import pathlib
import subprocess
import sys
import os
import gzip
import zipfile
import tarfile
import rarfile
import magic
import binwalk
import shutil
from bin2ir3 import idarun
from bin2ir3 import transbin2IR
from enum import Enum
import copy
import re
import time

from extra.report import *
from extra.config import config

#statistical information
numdecompress = 0
numfirmware = 0
numextracted = 0

allruleresult = dict()
soset = dict()
execset = dict()
name2path = dict()
ousingrandset = dict()    # 保存只使用了 rand 而没有使用 srand 的程序

cryptlibset = {"libcrypto", "libcrypt", "libssl", "libgcrypt", "libwolfssl", "libmcrypt"}

class randtype(Enum):
    Orand = 1
    Osrand = 2
    Orsrand = 3
    Nrand = 4

class compressmethod(Enum):
    Egz = 0
    Etar = 1
    Etgz = 2
    Ezip = 3
    Erar = 4
    Edir = -2
    Eunknown = -1

def getcompressmethod(filename):
    result = compressmethod.Eunknown
    if os.path.isdir(filename):
        result = compressmethod.Edir
        return result
    filetype = _get_filetype(filename)
    if filetype == "application/gzip":
        result = compressmethod.Egz
    elif filetype == "application/x-tar":
        result = compressmethod.Etar
    elif filetype == "application/zip":
        result = compressmethod.Ezip
    elif filetype == "application/x-rar":
        result = compressmethod.Erar
    return result


def filenameformat(filename):
    filename = filename.replace("(","\\(")
    filename = filename.replace(")","\\)")
    return filename
    

def _get_filetype(data,mime=True):
    return magic.from_file(data,mime)

def un_gz(filename,outputpath):
    g_file = gzip.GzipFile(filename)
    dirname = path2filename(filename)
    open(outputpath +"/" + dirname , "wb+").write(g_file.read())
    g_file.close()
    return outputpath +"/" + dirname

def un_tar(filename,outputpath):
    tar = tarfile.open(filename)
    names = tar.getnames()
    dirname = path2filename(filename)
    if os.path.isdir(outputpath+"/" + dirname):
        pass
    else:
        os.mkdir(outputpath+"/"+dirname)
    for name in names:
        tar.extract(name,outputpath + "/" + dirname +"/")
    tar.close()
    return outputpath+"/" + dirname
    


def un_zip(file_name,outputpath):
    zip_file = zipfile.ZipFile(file_name)
    dirname = path2filename(file_name)
    if os.path.isdir(outputpath+"/" + dirname):
        pass
    else:
        os.mkdir(outputpath+"/" + dirname)
    for names in zip_file.namelist():
        try:
            zip_file.extract(names,outputpath+"/" + dirname+ "/")
        except zipfile.BadZipfile as err:
            print(err)
            print(outputpath+"/" + dirname)
    zip_file.close()
    return outputpath+"/" + dirname

def un_rar(filename,outputpath):
    rar = rarfile.RarFile(filename)
    dirname = path2filename(filename)
    if os.path.isdir(outputpath + "/" + dirname):
        pass
    else:
        os.mkdir(outputpath + "/" + dirname)
    pwd = os.getcwd()
    os.chdir(outputpath + "/" + dirname)
    rar.extractall()
    rar.close()
    os.chdir(pwd)
    return outputpath + "/" + dirname


def decompress(file_name,outputdir,dc = True):
    filetype = getcompressmethod(file_name)
    #print(file_name)
    global numdecompress
    if filetype == compressmethod.Ezip:
        try:
            if dc:
                numdecompress += 1
            un_zip(file_name,outputdir)
        except BaseException as err:
            print(file_name)
    elif filetype == compressmethod.Erar:
        try:
            un_rar(file_name,outputdir)
            if dc:
                numdecompress += 1
        except BaseException as err:
            print(file_name)
    elif filetype == compressmethod.Egz:
        tmpresult = un_gz(file_name,outputdir)
        if dc:
            numdecompress += 1
        filetype2 = getcompressmethod(tmpresult)
        if not filetype2 == compressmethod.Eunknown:
            decompress(tmpresult,outputdir,dc = False)
        os.remove(tmpresult)
    elif filetype == compressmethod.Etar:
        un_tar(file_name,outputdir)
        if dc:
            numdecompress += 1
    elif filetype == compressmethod.Etgz:
        pass
    elif filetype == compressmethod.Eunknown:
        shutil.copyfile(file_name, outputdir + getfilenamefrompath(file_name))
        pass
    return True

def nmfile(sofile):
    result = set()
    sofile =filenameformat(sofile)
    filetype = _get_filetype(sofile)
    if not filetype == "application/x-sharedlib":
        return result
    output = os.popen("nm -D " + sofile)
    allline = output.read().split("\n")
    for line in allline:
        field = line.split(" ")
        if not len(field) == 3 or not field[1] == "T":
            continue
        result.add(field[2])
    return result


def extractfile(filename,outputdir):
    filetype = _get_filetype(filename)
    if any(s in [filetype] for s in ["application/x-executable",
                    "application/x-dosexec",
                    "application/x-object",
                    "application/pdf",
                    "application/msword",
                    "image/", "text/", "video/"]):
        return
    filetype = _get_filetype(filename,mime=False)
    if any(s in [filetype] for s in ["executable", "universal binary",
                    "relocatable", "bytecode", "applet"]):
        return
    print(filename)
    pwd = os.getcwd()
    os.chdir(outputdir)
    global numfirmware
    numfirmware += 1
    
    # for module in binwalk.scan(filename,"-0","root","-e" ,"-y", "filesystem", signature=True, quiet=True, extract=True):
    for module in binwalk.scan(filename,"-e" ,"-y", "filesystem", signature=True, quiet=True, extract=True):
        for result in module.results:
            if result.file.path in module.extractor.output:
                if result.offset in module.extractor.output[result.file.path].extracted:
                    pass
    os.chdir(pwd)
    return True


def getfilenamefrompath(path):
    return path[path.rindex("/") + 1:len(path)]

class archtype(Enum):
    Elarm = 0
    Elmips = 1
    Eunknown = -1

def libformat(libname,filetype):
    result = ""
    if not filetype == "application/x-sharedlib":
        return result
    lindex = 0
    if not libname.find("/") == -1:
        lindex = libname.rindex("/")+1
    if not libname.find(".so") == -1:
        result = libname[lindex:libname.find(".so")].strip()
    elif not libname.find(".a") == -1:
        result = libname[lindex:libname.find(".a")].strip()
    else:
        result = libname[lindex:len(libname)]
    return result
    

def listallso(filename,arch):
    # soset = set()
    # commandstr = ""
    # if arch == archtype.Elmips:
    #     commandstr = "$HOME/buildroot/output/host/bin/ldd"
    # elif arch == archtype.Elarm:
    #     commandstr = "$HOME/armbuildroot/output/host/bin/ldd"
    # else:
    #     return soset
    # filename = filenameformat(filename)
    # (status,output) = subprocess.getstatusoutput( commandstr + ' ' + filename)
    # #print(output)
    # #print(filename)
    # #print(filename)
    # outstr = output.splitlines()
    # for line in outstr:
    #     if "=>" in line:
    #         soname = line.split("=>")[0]
    #         #print(soname)
    #         if not soname.find(".so") == -1:
    #             soname = soname[:soname.find(".so")].strip()
    #         elif not soname.find(".a") == -1:
    #             soname = soname[:soname.find(".a")].strip()
    #         soset.add(soname)
    # return soset
    soset = set()
    filename = filenameformat(filename)
    # print('list so from: ' + filename)
    output = subprocess.getoutput('readelf -a ' + filename + ' | grep \"Shared library\"')
    outlines = output.splitlines()
    for line in outlines:
        so = line.split()[-1].replace('[', '').replace(']', '')
        so = so.split('.')[0]
        soset.add(so)
        # print('Shared lib: ' + so)
    return soset
    
def _getarch(filename):
    result = archtype.Eunknown
    filetype = ""
    filename = filenameformat(filename)
    filetype = _get_filetype(filename)
    if not any(s in [filetype] for s in ["application/x-executable","application/x-sharedlib"]):
        return result
    (status,output) = subprocess.getstatusoutput('readelf -h ' + filename)
    outstr = output.splitlines()
    if not len(outstr) > 9:
        return result
    fields=outstr[8].split()
    if not len(fields) > 1:
        return result
    if fields[1] == "ARM":
        result = archtype.Elarm
    elif fields[1] == "MIPS":
        result = archtype.Elmips
    return result

def isusecrypt(filename,arch):
    filename = filenameformat(filename)
    result = False
    if arch == archtype.Elarm:
        (status,output) = subprocess.getstatusoutput('armobjdump.sh ' + filename + " | grep -E -i \"gcry|EVP|CAST|SSL|encry|cry|aes|DES|decry\"")
        if(len(output) > 0):
            outstr = output.splitlines()
            outputline = filename
            for line in outstr:
                allfield = line.split()
                if(len(allfield) == 2):
                    outputline += " " + allfield[1][0:len(allfield[1])-1]
            print(outputline)
            result = True
    elif arch == archtype.Elmips:
        (status,output) = subprocess.getstatusoutput('mipsobjdump.sh ' + filename + " | grep -E -i \"gcry|EVP|CAST|SSL|encry|cry|aes|DES|decry\"")
        if(len(output) > 0):
            outstr = output.splitlines()
            outputline = filename
            for line in outstr:
                    allfield = line.split()
                    if(len(allfield) == 2): 
                            outputline += " " + allfield[1][0:len(allfield[1])-1]
            print(outputline)
            result = True
    else:
        pass
    return result

def filterfile(filename,outputdir):
    arch = _getarch(filename)
    #print(filename)
    #soset = listallso(filename,arch)
    #if len(soset) == 0:
    #    return
    '''for so in soset:
        
        if "libgcry" in so or "libcry" in so or "libssl" in so or "libgcry" in so: 
            shutil.copyfile(filename, outputdir + getfilenamefrompath(filename))
            #print(filename)
            break
        #print(so)'''
    #print(filename)
    if isusecrypt(filename,arch):
        shutil.copyfile(filename, outputdir + getfilenamefrompath(filename))
    return True


def translateIR(filename,outputdir,importfc = dict()):
    '''print(filename)
    filetype = _get_filetype(filename)
    filename = filenameformat(filename)
    outputdir = filenameformat(outputdir)
    onlyfilename = getfilenamefrompath(filename)
    #option = 0
    if onlyfilename == "busybox":
        return
    if not any(s in [filetype] for s in [b"application/x-executable",
                     b"application/x-object",b"application/x-sharedlib"]):
        #print(filename)
        return
    if filetype == b"application/x-executable":
        option = 0
    elif filetype ==  b"application/x-sharedlib":
        option = 1
    elif filetype == b"application/x-object":
        option = 1
        if filename.endswith(".ko"):
            option = 2
    outputfile = outputdir + "/" + onlyfilename+"ir"
    print("python angrir.py " + filename + " " + outputfile  + " > " + outputfile)
    os.system("python angrir.py " + filename + " " + outputfile  + " > " + outputfile)
    return'''
    onlyfilename = getfilenamefrompath(filename)
    outputfile = outputdir + "/" + onlyfilename
    return transbin2IR(filename,outputfile,importfc)

def getIRtmp(filename,outputdir):
    arch = _getarch(filename)
    #print(filename)
    #soset = listallso(filename,arch)
    #print(soset)
    filetype = _get_filetype(filename)
    filename = filenameformat(filename)
    outputdir = filenameformat(outputdir)
    onlyfilename = getfilenamefrompath(filename)
    if onlyfilename == "busybox":
        return
    if not any(s in [filetype] for s in ["application/x-executable",
                        "application/x-object","application/x-sharedlib"]):
        return
    outputdir += onlyfilename
    idarun(filename,outputdir)
    return True
    


def challown(filename):
    filename = filenameformat(filename)
    os.ystem("chown $USER:$USER " + filename)


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def getfileowner(filename):
    filename = filenameformat(filename)
    (status,output) = subprocess.getstatusoutput('ls -al ' + filename)
    print(filename)
    print(output)
    result = output.split()[2]
    return result

''' keep dir struct'''
def dfs_dir(path,outputpath,operationf = None,operationd = None):
    stack = []
    ret = []
    stack.append(path)
    if not outputpath == None:
        mkdir(outputpath)
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        #print(tmp)
        try:
            if(os.path.isdir(tmp)):
                print(tmp)
                #ret.append(tmp)
                Doutputpath = tmp[tmp.index(path)+len(path):tmp.rindex("/")]
                destpath = ""
                if Doutputpath == "":
                    destpath = outputpath + "/"
                else:
                    destpath = outputpath + "/" + Doutputpath + "/"
                if not operationd == None:
                    operationd(tmp,destpath)
                for item in os.listdir(tmp):
                    fullfilenamestr = os.path.join(tmp,item)
                    stack.append(fullfilenamestr)
            elif(os.path.isfile(tmp)):
                #print(tmp)
                ret.append(tmp)
                Doutputpath = tmp[tmp.index(path)+len(path):tmp.rindex("/")]
                destpath = ""
                if Doutputpath == "":
                    destpath = outputpath + "/"
                else:
                    destpath = outputpath + "/" + Doutputpath + "/"
                mkdir(destpath)
                if not operationf == None:
                    operationf(tmp,destpath)
        except IOError:
            print(tmp)
    return ret

def path2filename(path):
    fullfilename = path[path.rindex("/")+1:len(path)]
    prefixfilename = fullfilename[0:fullfilename.rindex(".")]
    return prefixfilename

def usingrand(fullformatname):
    result=randtype.Nrand
    output = os.popen("nm -D " + fullformatname)
    regex = re.compile('\s+')
    allline = output.read().split("\n")
    functionset = set()
    for line in allline:
        field = regex.split(line)
        if not len(field) == 3 or not field[1] == "U":
            continue
        functionset.add(field[2].strip())
    # if "rand" in functionset and ("srand" in functionset or "srandom" in functionset):
    if "rand" in functionset and "srand" in functionset:
        result = randtype.Orsrand
    elif "rand" in functionset:
        result = randtype.Orand
    elif "srand" in functionset:
        result = randtype.Osrand
    return result

#def rootfinddfs(path,dirname,soset,execset):
def soexecfile(fullname,outputdir):
    global soset
    global execset
    global name2path
    fullname = filenameformat(fullname)
    filetype = _get_filetype(fullname)
    arch = _getarch(fullname)
    filename = ""
    if fullname.find("/") == -1:
        filename = fullname
    else:
        filename = fullname[fullname.rindex("/")+1:len(fullname)]
    #print(filename + ' ' +filetype)
    if filetype == "application/x-executable":
        #print(filename + ' ' +filetype)
        allso = listallso(fullname,arch)
        #print(allso)
        for allsoitem in allso:
            if not allsoitem in execset:
                execset[allsoitem] = set()
            execset[allsoitem].add(filename)
        name2path[filename] = fullname
        if usingrand(fullname) == randtype.Orand:
            ousingrandset[filename] = fullname
        #execset[allso] = filename
    elif filetype == "application/x-sharedlib":
        #print(filename + ' ' +filetype)
        filename = libformat(fullname,filetype)
        allso = listallso(fullname,arch)
        for allsoitem in allso:
            if not allsoitem in soset:
                soset[allsoitem] = set()
            soset[allsoitem].add(filename)
        name2path[filename] = fullname
        if usingrand(fullname) == randtype.Orand:
            ousingrandset[filename] = fullname
        #soset[allso] = filename
    return True

def wdetail(df,prompt,dinfo=dict()):
    wfd = open(df,"a")
    wfd.write(prompt+"\n")
    for item in dinfo:
        wfd.write(dinfo[item][0]+"\n")
    wfd.close()

def wfsummury(sf,prompt,sdict = dict()):
    if sf == None:
        wfd = sys.stdout
    else:
        wfd = open(sf,"a")
    wfd.write(str(prompt)+"\n")
    for item in sdict:
        wfd.write(item + " " + str(sdict[item]) + "\n")
    wfd.close()

def summurycount(dinfo,result):
    for ditemindex in dinfo:
        ditem = dinfo[ditemindex]
        print(ditem[1])
        print(ditem[2])
        if not str(ditem[1]) + " " + str(ditem[2]) in result:
            result[str(ditem[1]) + " " + str(ditem[2])] = 1
        else:
            result[str(ditem[1]) + " " + str(ditem[2])] += 1
        if not str(ditem[1]) + " " + str(ditem[2]) in allruleresult:
            allruleresult[str(ditem[1]) + " " + str(ditem[2])] = 1
        else:
            allruleresult[str(ditem[1]) + " " + str(ditem[2])] += 1

def systemconstruct(dirfullpath,outputdir):
    # > /root/Downloads/Output/extract/all_packages-mipsbe-6.42.9/_ppp-6.42.9-mipsbe.npk.extracted
    # > /root/Downloads/Output/ir//all_packages-mipsbe-6.42.9/
    global soset
    global execset
    global cryptlibset
    global name2path
    global ousingrandset
    dirname = ""
    result = True
    currentset = cryptlibset
    currentnextset = set()
    allfset = currentset
    alleset = set()
    alldepend=dict()
    summtable=dict()
    writefirst = True
    if dirfullpath.find("/") == -1:
        dirname = dirfullpath
    else:
        dirname = dirfullpath[dirfullpath.rindex("/") + 1:len(dirfullpath)]
    print(dirname)
    if dirname.endswith("extracted"):
        testbegintime = time.time()
        transtimesum = 0
        firmname = dirname[0:dirname.find(".extracted")]
        
        filloutputdir = ""
        if not dirfullpath.find("/") == -1:
            filloutputdir = outputdir + "/" + dirfullpath[dirfullpath.rindex("/") + 1:]
        else:
            filloutputdir = outputdir
        detailreportfile = filloutputdir + ".dreport"
        summuaryreportfile = filloutputdir + ".summary"
        global numextracted
        numextracted += 1
        result = False
        soset.clear()
        execset.clear()
        name2path.clear()
        ousingrandset.clear()
        
        
        # Traverse all extracted files
        # Map imported libraries -> execuables/libraries importing them
        # Problem-1 lies in here, that is, 
        # yielding static rand seed usage only because rand & srand are not both imported
        # e.g.
        # soset: {'libc': {'libcrypt', 'q_netem', 'libid3tag', 'libavutil', 'libssl', 'libavdevice', 'libFLAC', 'libcrypto', 'libexif', 'libutil', 'libvorbis', 'libbigballofmud', 'libavformat', 'libvolume_id', 'libdl', 'libnsl', 'openvpn-plugin-down-root', 'libavcodec', 'libsqlite3', 'libgcc_s', 'libm', 'libogg', 'libpthread', 'libresolv', 'libjpeg', 'libz'}, 'ld-uClibc': {'libc', 'libpthread', 'libdl'}, 'libm': {'libFLAC', 'libavcodec', 'libexif', 'libavutil', 'libvorbis', 'libavformat'}, 'libdl': {'libssl', 'libbigballofmud', 'libcrypto', 'libsqlite3'}, 'libcrypto': {'libssl'}, 'libgcc_s': {'libFLAC', 'libcrypto', 'libavformat', 'libsqlite3', 'libavcodec', 'libavutil', 'libbigballofmud', 'libavdevice'}, 'libogg': {'libFLAC', 'libvorbis'}, 'libpthread': {'libsqlite3'}, 'libavcodec': {'libavdevice', 'libavformat'}, 'libavutil': {'libavdevice', 'libavformat', 'libavcodec'}, 'libavformat': {'libavdevice'}, 'libz': {'libid3tag', 'libavformat', 'libavcodec'}, 'libnvram': {'openvpn-plugin-down-root'}, 'libcrypt': {'libbigballofmud'}, 'libresolv': {'libbigballofmud'}}
        # execset: {'libvolume_id': {'vol_id'}, 'libc': {'acos_service', 'ntpclient', 'eapd', 'autoipd', 'dnsmasq', 'acsd', 'igs', 'bd', 'mld', 'udhcpd', 'zipinfo', 'scheact', 'openvpn', 'wlconf', 'udevtrigger', 'wps_monitor', 'gproxy', 'gpio', 'brctl', 'dhcp6s', 'tc', 'smb_pass', 'xtables-multi', 'bftpd', 'heartbeat', 'acs_cli', 'pot', 'dnsRedirectReplyd', 'busybox', 'acl_logd', 'l2tpd', 'mevent', 'lld2d', 'ubdcmd', 'wlanconfigd', 'pppd', 'et', 'swresetd', 'upnpd', 'bzip2', 'vconfig', 'parser', 'vol_id', 'ses_cl', 'httpd', 'wl', 'tcpdump', 'ftpc', 'tfmeter', 'zeroconf', 'ip6tables-save', 'nas', 'vmstat', 'tcpdump.4.4.0', 'ip', 'IPv6-relay', 'rc', 'ses', 'zebra', 'zipsplit', 'radvd', 'dlnad', 'nvram', 'minidlna.exe', 'zipnote', 'pppoecd', 'ripd', 'emf', 'unzipsfx', 'wpsd', 'utelnetd', 'ddnsd', 'unzip', 'nmbd', 'outputimage', 'taskset', 'hotplug2', 'pptp', 'smbd', 'check_fw', 'ip6tables', 'dhcp6c', 'ip6tables-restore', 'timesync', 'htmlget', 'cli', 'wandetect', 'wan_debug', 'telnetenabled', 'funzip', 'rtsol', 'zipcloak', 'email', 'zip', 'wget'}, 'libcrypt': {'smb_pass', 'upnpd', 'busybox', 'smbd', 'nmbd', 'pppd', 'bftpd', 'httpd'}, 'libdl': {'minidlna.exe', 'smb_pass', 'tc', 'smbd', 'pppd', 'openvpn', 'nmbd', 'wget'}, 'libacos_shared': {'wpsd', 'ddnsd', 'httpd', 'outputimage', 'acos_service', 'heartbeat', 'pot', 'dnsRedirectReplyd', 'acl_logd', 'ftpc', 'autoipd', 'mevent', 'lld2d', 'check_fw', 'timesync', 'bd', 'tfmeter', 'ubdcmd', 'wandetect', 'scheact', 'wlanconfigd', 'rc', 'upnpd', 'wan_debug', 'gproxy', 'telnetenabled', 'email', 'rtsol', 'dlnad', 'parser'}, 'libnvram': {'ses_cl', 'wpsd', 'ddnsd', 'bftpd', 'httpd', 'outputimage', 'acos_service', 'heartbeat', 'acs_cli', 'pot', 'dnsRedirectReplyd', 'eapd', 'acl_logd', 'ftpc', 'autoipd', 'mevent', 'lld2d', 'check_fw', 'acsd', 'timesync', 'bd', 'mld', 'tfmeter', 'nas', 'ubdcmd', 'wandetect', 'scheact', 'wlanconfigd', 'openvpn', 'swresetd', 'wlconf', 'rc', 'ses', 'upnpd', 'wps_monitor', 'wan_debug', 'gproxy', 'gpio', 'telnetenabled', 'email', 'rtsol', 'dlnad', 'nvram', 'parser'}, 'libgcc_s': {'minidlna.exe', 'smb_pass', 'xtables-multi', 'ses_cl', 'wpsd', 'ddnsd', 'httpd', 'outputimage', 'acos_service', 'heartbeat', 'acs_cli', 'tcpdump', 'pot', 'dnsRedirectReplyd', 'eapd', 'busybox', 'smbd', 'acl_logd', 'ftpc', 'autoipd', 'mevent', 'lld2d', 'check_fw', 'ip6tables', 'acsd', 'ip6tables-restore', 'timesync', 'bd', 'mld', 'tfmeter', 'ip6tables-save', 'nas', 'ubdcmd', 'wandetect', 'scheact', 'wlanconfigd', 'vmstat', 'swresetd', 'tcpdump.4.4.0', 'wlconf', 'rc', 'tc', 'ses', 'upnpd', 'wps_monitor', 'wan_debug', 'gproxy', 'gpio', 'telnetenabled', 'email', 'rtsol', 'brctl', 'dlnad', 'parser', 'wget'}, 'libbcm': {'rc', 'ses', 'ses_cl', 'wps_monitor', 'gpio', 'swresetd'}, 'libshared': {'mld', 'rc', 'heartbeat', 'acs_cli', 'ses', 'nas', 'eapd', 'ses_cl', 'wps_monitor', 'acl_logd', 'gpio', 'mevent', 'dlnad', 'swresetd', 'wlconf', 'acsd'}, 'libbcmcrypto': {'mld', 'rc', 'ses', 'nas', 'ses_cl', 'wps_monitor', 'acl_logd'}, 'libnat': {'acos_service', 'tfmeter', 'heartbeat', 'upnpd', 'cli', 'ubdcmd', 'wandetect', 'email', 'mevent', 'check_fw', 'httpd'}, 'libresolv': {'openvpn', 'smb_pass', 'smbd', 'nmbd'}, 'libbigballofmud': {'nmbd', 'smbd'}, 'libcrypto': {'tcpdump', 'openvpn', 'tcpdump.4.4.0', 'bftpd', 'httpd', 'wget'}, 'libnsl': {'openvpn'}, 'libssl': {'openvpn', 'httpd', 'wget'}, 'libz': {'openvpn', 'minidlna.exe'}, 'libpthread': {'minidlna.exe', 'gproxy'}, 'libutil': {'pptp', 'outputimage'}, 'libm': {'minidlna.exe', 'ip6tables-save', 'xtables-multi', 'busybox', 'wps_monitor', 'ip6tables', 'ip6tables-restore', 'tc'}, 'libip4tc': {'ip6tables', 'xtables-multi', 'ip6tables-restore', 'ip6tables-save'}, 'libxtables': {'ip6tables', 'xtables-multi', 'ip6tables-restore', 'ip6tables-save'}, 'libip6tc': {'ip6tables', 'xtables-multi', 'ip6tables-restore', 'ip6tables-save'}, 'libFLAC': {'minidlna.exe'}, 'libavformat': {'minidlna.exe'}, 'libsqlite3': {'minidlna.exe'}, 'libavcodec': {'minidlna.exe'}, 'libexif': {'minidlna.exe'}, 'libid3tag': {'minidlna.exe'}, 'libavutil': {'minidlna.exe'}, 'libogg': {'minidlna.exe'}, 'libvorbis': {'minidlna.exe'}, 'libjpeg': {'minidlna.exe'}, 'libupnp': {'wps_monitor'}}
        dfs_dir(dirfullpath,outputdir+"/"+dirname,operationf=soexecfile,operationd=None)
        # dbg(f'soset: {soset}\nexecset: {execset}')

        for cryptolib in cryptlibset:
            s = report.cryptolib_imported[cryptolib]
            if cryptolib in soset:
                s = s.union(soset[cryptolib])
            if cryptolib in execset:
                s = s.union(execset[cryptolib])
            report.cryptolib_imported[cryptolib] = s

        # currentset = {"libcrypto", "libcrypt", "libssl", "libgcrypt", "libwolfssl", "libmcrypt"}
        # Find those libraries in firmware that import specific cryptographic libraries
        # e.g.
        # currentnextset: {'libssl', 'libbigballofmud'}
        for currentitem in currentset:
            if currentitem in soset:
                loadsoset = soset[currentitem]
                currentnextset = currentnextset.union(loadsoset)
                
        # dbg(f'currentnextset: {currentnextset}')
        # Totally in a mess...
        # Traverse all libraries, construct an inter-procedural cfg and perform taint analysis
        while len(currentnextset) > 0:
            currentset = copy.copy(currentnextset)
            currentnextset.clear()
            for currentitem in currentset:
                if currentitem in allfset or currentitem == "cupsd" or currentitem == "libtorrent-rasterbar" or currentitem == "smbd" or currentitem == "libperl" or currentitem == "libphp5" or currentitem == "libapr-1":# or currentitem == "tdbbackup" or currentitem == "net" or currentitem == "libbigballofmud" or  currentitem == "smbpasswd" or currentitem == "libsysctxlua" or currentitem == "libzebra" or currentitem == "libcurl" or currentitem == "ssl" or currentitem == "zebra" or currentitem == "stunnel" or currentitem == "libntpass":
                    continue
                onlyfilename = getfilenamefrompath(name2path[currentitem])
                # Ignore libraries whose size are greater than 10 MB
                if os.path.getsize(name2path[currentitem]) // float(1024*1024) > 10:
                    continue
                
                # Correspond to "3.2 Lifting to VEX IR" in paper
                # This part aims to address the following 3 problems in angr
                # (1) The call relations of Angr is incomplete because it only considers explicit invocation addresses. 
                #     If the address isput into a register or memory, Angr cannot locate it. 
                # (2) Type information of variables is lost, which affects the data-flow tracking 
                #     (especially the function parameters). 
                # (3) The function arguments are often passed via the register, 
                #     stack, or both, and follow specific conventions. If the binary code 
                #     is lifted to the IR, architecture-specific calling convention will be lost.
                
                # Stage-3: Running idc script
                a = time.time()
                getIRtmp(name2path[currentitem],filloutputdir + "/")
                b = time.time()
                report.stage3_time += b - a
                
                testbegintime2 = time.time()
                # [!!!] Perform taint analysis here
                (exporteddic,detailreport) = translateIR(filloutputdir + "/" + onlyfilename + "idcom",filloutputdir)
                testendtime2 = time.time()
                transtimesum += (testendtime2 - testbegintime2)
                if not len(detailreport) == 0 and writefirst:
                    writefirst = False
                    wdetail(detailreportfile,firmname)
                    wdetail(detailreportfile,currentitem)
                    wdetail(detailreportfile,name2path[currentitem],detailreport)
                    summurycount(detailreport,summtable)
                elif not len(detailreport) == 0:
                    wdetail(detailreportfile,currentitem)
                    wdetail(detailreportfile,name2path[currentitem],detailreport)
                    summurycount(detailreport,summtable)
                alldepend[currentitem] = exporteddic
                if currentitem in soset:
                    loadsoset = soset[currentitem]
                    currentnextset = currentnextset.union(loadsoset)
            allfset = allfset.union(currentset)
        for allfitem in allfset:
            if allfitem in execset:
                alleset = alleset.union(execset[allfitem])
        print("------")
        print(alleset)
        # Traverse all executables, construct an inter-procedural cfg and perform taint analysis
        for execitem in alleset:
            if execitem.startswith("openssl") or execitem == "ssh" or execitem == "smbd" or execitem == "perl" or execitem.find("php") == 0 or execitem == "mysqld" or execitem == "pppd" or execitem == "vsftpd" or execitem == "busybox" or execitem == "stunnel" or execitem == "zebra" or execitem == "email" or execitem == "sshd" or execitem == "ldapwhoami" or execitem == "mount.cifs":# or execitem == "httpd" or execitem == "dhclient" or execitem == "guardian" or execitem == "jnap" or execitem == "fwupd" or execitem == "curl" or execitem == "sshd" or execitem == "wget":#wgets for 360
                continue
            if os.path.getsize(name2path[execitem]) // float(1024*1024) > 10:
                continue
            print(execitem)
            so = listallso(name2path[execitem],_getarch(name2path[execitem]))
            importedso = dict()
            for soitem in so:
                if soitem in alldepend:
                    importedso.update(alldepend[soitem])
                   
            # Stage-3: Running idc script
            a = time.time()
            getIRtmp(name2path[execitem],filloutputdir+"/")
            b = time.time()
            report.stage3_time += b - a
            
            onlyfilename = getfilenamefrompath(name2path[execitem])
            testbegintime2 = time.time()
            (exporteddic,detailreport) = translateIR(filloutputdir + "/" + onlyfilename + "idcom",filloutputdir,importedso)
            testendtime2 = time.time()
            transtimesum += (testendtime2 - testbegintime2)
            if not len(detailreport) == 0 and writefirst:
                writefirst = False
                wdetail(detailreportfile,firmname)
                wdetail(detailreportfile,execitem)
                wdetail(detailreportfile,name2path[execitem],detailreport)
                summurycount(detailreport,summtable)
            elif not len(detailreport) == 0:
                    wdetail(detailreportfile,execitem)
                    wdetail(detailreportfile,name2path[execitem],detailreport)
                    summurycount(detailreport,summtable)
            print("Detailed Report:")
            print(detailreport)
        testendtime = time.time()
        print("systemconstructtime %f"%(testendtime - testbegintime - transtimesum))
        detailre = dict()
        #print(name2path)
        for randitem in ousingrandset:
            report.vulnerabilities.append(ViolationDetail(name2path[randitem], "rand", [], [0,], "rand() without srand()", 5))
            detailre[randitem] = ("using static seed for rand",5,"using static seed for rand")
            wdetail(detailreportfile,name2path[randitem],detailre)
            summurycount(detailre,summtable)
        #print(summtable)
        wfsummury(summuaryreportfile,firmname,summtable)
    
    return result
    

if __name__ == "__main__":
    
    start_time = time.time()
    
    if not len(sys.argv) == 2:
        print("Usage: python bin2vex.py <input_file>");
        sys.exit(-1);
    
    # Input: single firmware
    inputpath = f'{config.working_dir}/input/{sys.argv[1]}'
    # Onput: detailed report
    init(report_path=f'{config.working_dir}/report/{sys.argv[1]}.log')
    
    # Those files are not important
    tmppath = f'{config.working_dir}/tmp/tmp/{sys.argv[1]}'
    outputpath = f'{config.working_dir}/tmp/extract/{sys.argv[1]}'
    irpath = f'{config.working_dir}/tmp/ir/{sys.argv[1]}'
    for path in [tmppath, outputpath, irpath]:
        pathlib.Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
    
    # Stage-1: Decompressing
    a = time.time()
    testr = dfs_dir(inputpath, tmppath, operationf=decompress, operationd=None);
    b = time.time()
    report.stage1_time = b - a
    
    # Stage-2: Extracting
    a = time.time()
    testr = dfs_dir(tmppath, outputpath, operationf=extractfile, operationd=None);
    b = time.time()
    report.stage2_time = b - a
    
    testr = dfs_dir(outputpath, irpath, operationf=None, operationd=systemconstruct);
    
    end_time = time.time()
    report.total_time = end_time - start_time
    
    wfsummury(None,"allsummary",allruleresult);
    
    if report.stage5_time > 0:
        report.save()
        if len(report.vulnerabilities) > 0:
            global_report.save(report)

    