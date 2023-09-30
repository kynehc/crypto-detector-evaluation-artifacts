import os
import sys
import angr
import re
import copy
import magic
import binascii
import time
from problock import *

from extra.report import *
from extra.config import config

starttime = ""
def _get_filetype(data,mime=True):
    return magic.from_file(data,mime)

def filenameformat(filename):
    result = filename
    result = result.replace("(","\\(")
    result = result.replace(")","\\)")
    return result

def getdir(filename):
    result = ""
    if not filename.find("/") == -1:
        result = filename[0:filename.rindex("/")]
    else:
        pass
    return result

def getname(filename):
    result = ""
    if not filename.find("/") == -1:
        result = filename[filename.rindex("/") + 1:len(filename)]
    return result

def getidbfilename(filename,posfix):
    dirname = getdir(filename)
    name = getname(filename)
    if not name.find(".") == -1:
        name = name[0:name.rindex(".")] + posfix
    else:
        name += posfix
    result = dirname + "/" + name
    return result
    

def rmtmpfile(filename):
    filename = filenameformat(filename)
    idbfilename = getidbfilename(filename,".idb")
    asmfilename = getidbfilename(filename,".asm")
    os.remove(idbfilename)
    os.remove(asmfilename)
    

def idarun(filename, tmpname):
  filename = filenameformat(filename)
  idbfilename = getidbfilename(filename,".idb")
  tmpname += "idcom"
  #if not os.path.exists(tmpname):
  #  os.makedir(tmpname)
    # print("$HOME/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/idaq -B " + filename)
    # os.system("$HOME/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/idaq -B " + filename)
    # print("$HOME/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/idaq -S\"/media/vezir/b2552981-cae5-4a83-9f27-2d07beede43e/CRYPTOREX/idascript/bin2iridc.idc " + tmpname + "\" " + idbfilename)
    # os.system("$HOME/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/idaq -S\"/media/vezir/b2552981-cae5-4a83-9f27-2d07beede43e/CRYPTOREX/idascript/bin2iridc.idc " + tmpname + "\" " + idbfilename)
  os.system(config.ida_path + "/idal -B " + filename)
    #print(config.ida_path + "/idaq -S " + config.script_path + "\" " + tmpname + "\\" + idbfilename)
    #os.system("$HOME/Downloads/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/IDA_Pro_v6.4_\(Linux\)_and_Hex-Rays_Decompiler_\(ARM\)/idaq -S\"/media/vezir/b2552981-cae5-4a83-9f27-2d07beede43e/CRYPTOREX/idascript/bin2iridc.idc " + tmpname + "\" " + idbfilename)
  os.system(config.ida_path + "/idal -S\"" + config.script_path + " " + tmpname + "\" " + idbfilename)
  #os.system(config.ida_path + "/idaq -S\"" + config.script_path + "\" " + idbfilename)
  rmtmpfile(filename)

class FILETYPE:
    Vxexec = 1,
    Vlibobj = 2

ARCHD=["DCD","DCB","DC",".ascii",".word"]

def binlcominfo(filename):
    #result
    binfile = ""
    functionmap = functioncontainer()
    allfunction = list()
    allfunctionname = dict()
    lcom = dict()
    pltstype = dict()
    rodatatype = dict()
    datatype = dict()
    functiondata = dict()
    functionsp = dict()
    innerfunctions = dict()
    externfunctions = dict()
    alldata = dict()
    externfuncset = set()

    #flag
    binfileflag = True
    allfunctionflag = False
    lcomflag = False
    pltflag = False
    rodataflag = False
    dataflag = False
    functiondataflag = False
    rfd = open(filename,"rb")
    offset = 0
    resulttype = ""
    while 1:
        line = rfd.readline().strip()
        try:
            line = line.decode('UTF-8')
        except Exception:
            line = str(line)[2:-2]
            print(f'No UTF-8: {line}')
        if not line:
            break
        if line == "all function:":
            binfileflag = False
            allfunctionflag = True
            lcomflag = False
            pltflag = False
            rodataflag = False
            dataflag = False
            functiondataflag = False

            continue
        if line == "lcom":
            binfileflag = False
            allfunctionflag = False
            lcomflag = True
            pltflag = False
            rodataflag = False
            dataflag = False
            functiondataflag = False

            continue
        if line == "pltfunctiontype":
            binfileflag = False
            allfunctionflag = False
            lcomflag = False
            pltflag = True
            rodataflag = False
            dataflag = False
            functiondataflag = False

            continue
        if line == ".rodata":
            binfileflag = False
            allfunctionflag = False
            lcomflag = False
            pltflag = False
            rodataflag = True
            dataflag = False
            functiondataflag = False

            continue
        if line == ".data":
            binfileflag = False
            allfunctionflag = False
            lcomflag = False
            pltflag = False
            rodataflag = False
            dataflag = True
            functiondataflag = False

            continue
        if line == "functionenddata":
            binfileflag = False
            allfunctionflag = False
            lcomflag = False
            pltflag = False
            rodataflag = False
            dataflag = False
            functiondataflag = True

            continue

        if(binfileflag):
            binfile = line
            resulttype,offset = execorlib(binfile)
        elif(allfunctionflag):
            field = line.split("\t")
            if not (len(field) == 2 or len(field) == 3):
                continue
            funcaddr = int(field[0],16) + offset
            allfunction.append(funcaddr)
            beginsp = field[1].split(":")
            if len(beginsp) == 2:
                functionsp[int(field[0],16) + offset] = beginsp[1].strip()
            innerfunctions[beginsp[0]] = int(field[0],16) + offset
            tmpfunction = function()
            funcn = beginsp[0].strip()
            tmpfunction.setfunctionname(funcn)
            allfunctionname[funcaddr]=funcn
            tmpfunction.addfunctionaddr(int(field[0],16)+offset)
            tmpfunction.setfunctiontype(FUNCTIONTYPE.inner)
            functionmap.addfunction(tmpfunction)
        elif(lcomflag):
            field = re.split("\s+",line)
            #print(field)
            if not len(field) == 2:
                continue
            lcom[int(field[0],16)+offset] = field[1]
        elif(pltflag):
            field = line.split("\t")
            if not (len(field) == 2 or len(field) == 3):
                continue
            tmp = ""
            tmpl = list()
            tmpfunction = function()
            functionname = field[1].strip()
            if functionname.startswith("j_") and not functionmap.getfunction(functionname[0+len("j_"):len(functionname)]) == None:
                tmpfunction = functionmap.getfunction(functionname[0+len("j_"):len(functionname)])
                tmpfunction.addfunctionaddr(int(field[0],16) + offset)
                functionmap.addfunctionaddr(tmpfunction.getfunctionname(),int(field[0],16) + offset)
                continue
            else:
                tmpfunction.setfunctiontype(FUNCTIONTYPE.extern)
                tmpfunction.addfunctionaddr(int(field[0],16) + offset)
                externfuncset.add(field[1].strip())
            tmpfunction.setfunctionname(field[1].strip())
            if len(field) == 2:
                tmp = [field[1],tmpl]
            elif len(field) == 3:
                tmpl = re.split("[(),]",field[2])
                for tmpli in range(0,len(tmpl)):
                    tmpl[tmpli] = tmpl[tmpli].strip()
                    if tmpli == 0:
                        tmpfunction.setreturntype(tmpl[tmpli].strip())
                        #print(functionname)
                        #print("return type")
                        #print(tmpl[tmpli].strip())
                    else:
                        tmpfunction.addarg(tmpl[tmpli].strip())
                tmp = [field[1],tmpl]
                externfunctions[field[1]] = int(field[0],16) + offset
            pltstype[int(field[0],16) + offset] = tmp
            functionmap.addfunction(tmpfunction)
        elif(rodataflag):
            field = line.split("\t")
            if not len(field) == 2:
                continue
            rodatatype[int(field[0],16) + offset] = field[1]
            for aitem in ARCHD:
                if field[1].startswith(aitem) and not field[1].find(" ") == -1:
                    blanklocat = field[1].find(" ")
                    alldata[int(field[0],16) + offset] = field[1][blanklocat:len(field[1])].strip()
                    break
                elif field[1].startswith(aitem):
                    alldata[int(field[0],16) + offset] = field[1][len(aitem):len(field[1])].strip()
                    break
        elif(dataflag):
            field = line.split("\t")
            if not len(field) == 2:
                continue
            datatype[int(field[0],16) + offset] = field[1]
            for aitem in ARCHD:
                if field[1].startswith(aitem) and not field[1].find(" ") == -1:
                    blanklocat = field[1].find(" ")
                    alldata[int(field[0],16) + offset] = field[1][blanklocat:len(field[1])].strip()
                    break
                elif field[1].startswith(aitem):
                    alldata[int(field[0],16) + offset] = field[1][len(aitem):len(field[1])].strip()
                    break
        elif(functiondataflag):
            field = line.split("\t")
            if not len(field) == 2:
                continue
            tmpfield1 = field[1][field[1].find(" ") + 1:len(field[1])]
            #print(tmpfield1)
            if not field[1].startswith("DC") and field[1].isdigit():
                functiondata[int(field[0],16) + offset] = int(tmpfield1) + offset
                alldata[int(field[0],16) + offset] = int(tmpfield1) + offset
            else:
                functiondata[int(field[0],16) + offset] = tmpfield1
                alldata[int(field[0],16) + offset] = tmpfield1
    rfd.close()
    return binfile,allfunction,allfunctionname,lcom,pltstype,rodatatype,datatype,functiondata,functionsp,innerfunctions,externfunctions,functionmap,alldata,externfuncset

externfunctiondic = dict()

def nmfile(sofile):
        result = set()
        sofile =filenameformat(sofile)
        filetype = _get_filetype(sofile)
        if not filetype == b"application/x-sharedlib":
                return result
        output = os.popen("nm -D " + sofile)
        allline = output.read().split("\n")
        for line in allline:
                field = line.split(" ")
                if not len(field) == 3 or not field[1] == "T":
                        continue
                result.add(field[2])
        return result

nextblocktime = 0


def constructmycfg(node,proj,functionmap,lcom,mycfg,addrset,pathnode,test,bpspoffset, depth=1):
    if not node.beginaddr == 0:
        pathnode.append(node.beginaddr)
    #print("construct0x%X"%node.beginaddr)
    #print(node.beginaddr)
    global nextblocktime
    testa = time.time()
    bl = node.getnextblockaddr(bpspoffset)	# get successors of current block
    testb = time.time()
    nextblocktime += (testb - testa)
    resultleafnode=set()
    rightresultleafset=set()
    callset = set()
    for bitem in bl:	# traverse successors
        nextaddr = None
        nextnode = None
        tmpleaf = set()
        b=bitem[0]
        slide=bitem[1]
        f=functionmap.getfunction(b)
        if not f == None:
            if f.getfunctiontype() == FUNCTIONTYPE.inner:
                nextaddr = f.getfunctionaddr()[0]
            else:
                nextnode = problock()	# add a bogus block to reperesent a extern function
                nextnode.addexternflag()
                nextnode.addexternfun(f.getfunctionname())
                for a in f.getarg():
                    nextnode.addexternfunarg(a)
                if not f.getfunctionname() in externfunctiondic:
                    externfunctiondic[f.getfunctionname()] = list()
                externfunctiondic[f.getfunctionname()].append(nextnode)
        elif not b.isdigit():
            continue
        else:
            nextaddr = int(b)
        
        if (not nextaddr == None) and (not nextaddr in addrset):
            continue
        elif nextnode == None and nextaddr == None:
            continue
        elif nextnode == None and (not nextaddr == None):#inner
            block = proj.factory.block(nextaddr)
            irsb = block.vex
            nextnode = problock(irsb,lcom)
        if nextnode.beginaddr in pathnode:
            continue
        if (not nextaddr == None) and (not nextaddr == 0) and (nextaddr in mycfg):
            nextnode = mycfg[nextaddr][0]
            tmpleaf = mycfg[nextaddr][1]
        else:
            global starttime
            nowtime = time.time()
            if int(nowtime - starttime) // 60 <= 5:
                nextnode,tmpleaf = constructmycfg(nextnode,proj,functionmap,lcom,mycfg,addrset,copy.copy(pathnode),test+1,node.getbpspoffset(), depth=depth + 1)
                mycfg[nextaddr] = [nextnode,tmpleaf]
        resultleafnode=resultleafnode.union(tmpleaf)
        if slide == CHILDRENSIZE.Vexit:
            slideflag,locat = node.addleftchildren(nextnode)
            nextnode.addparents([node,slideflag,locat])
        elif slide == CHILDRENSIZE.Vnext:
            slideflag,locat = node.addrightchildren(nextnode)
            nextnode.addparents([node,slideflag,locat])
        elif slide == CHILDRENSIZE.Vlr:
            if nextaddr in callset:
                continue
            slideflag,locat = node.addrightchildren(nextnode)
            nextnode.addparents([node,slideflag,locat])
        if (not nextaddr == None) and (not nextaddr == 0):
            callset.add(nextaddr)
    if node.getleftchildren() == None and node.getrightchildren() == None:
        resultleafnode.add(node)
    return node,resultleafnode

def dfspp(node,time,s=""):
    msg = ""
    for i in range(0,time):
        msg += " "
    msg += str(time) + " " + s + " "
    msg += node.getmetadata()
    for pnode in node.getparents():
        msg += " 0x%X "%pnode[0].beginaddr
    print(msg)
    for cnode in node.getleftchildren():
        dfspp(cnode,time+1)
    for cnode in node.getrightchildren():
        dfspp(cnode,time+1)

def execorlib(filename):
    filetype = _get_filetype(filename)
    resulttype = ""
    #if any(s in [filetype] for s in [b"application/x-executable"]):
    if filetype == 'application/x-executable':
        #print("x-ex")
        wfiletype = "x-ex\n"
        offset = 0
        resulttype = FILETYPE.Vxexec
    #elif any(s in [filetype] for s in [b"application/x-sharedlib"]):
    elif filetype == 'application/x-sharedlib':
        #print("x-obj")
        wfiletype = "x-obj\n"
        offset = 0x400000
        resulttype = FILETYPE.Vlibobj
    return resulttype,offset

def execfunction():
    # functionfilename = "execfunction"
    functionfilename = config.execfunction_path
    functionfd = open(functionfilename,"r")
    functionfd = open(functionfilename,"r")
    funcnameset = set()
    funcdetail = dict()
    while True:
        line = functionfd.readline().strip()
        if not line:
            break
        if not len(line) == 0 and line[0] == "#":
            continue
        if len(line) == 0:
            continue
        field = line.split("\t")
        if not len(field) == 2:
            continue
        funcprototype = re.split("[(),]",field[0].strip())
        if len(funcprototype) == 0:
            continue
        funcheader = funcprototype[0].split(" ")
        if not len(funcheader) == 2:
            continue
        if funcheader[1][0] == "*":
            funcheader[1] = funcheader[1][1:len(funcheader[1])]
            funcheader[0] += "*"
        funcnameset.add(funcheader[1])
        tfop = funcop()
        tfop.setfunctionname(funcheader[1])
        tfop.setreturntype(funcheader[0])
        topfield = field[1].split(" ")
        for f in topfield:
            infodetailfield = f.split(":")
            if not len(infodetailfield) == 3:
                continue
            if infodetailfield[0].strip() == "dest":
                tfop.setfuncdest(int(infodetailfield[1]))
                if infodetailfield[2] == "string":
                    tfop.setdesttype(FARGTYPE.Vstring)
                elif infodetailfield[2] == "int":
                    tfop.setdesttype(FARGTYPE.Vint)
            elif infodetailfield[0].strip() == "src":
                tfop.setfuncsrc(int(infodetailfield[1]))
                if infodetailfield[2] == "string":
                    tfop.setsrctype(FARGTYPE.Vstring)
                elif infodetailfield[2] == "int":
                    tfop.setsrctype(FARGTYPE.Vint)
            elif infodetailfield[0].strip() == "len":
                tfop.setfunclen(int(infodetailfield[1]))
        funcdetail[funcheader[1]] = tfop
    functionfd.close()
    return funcnameset,funcdetail
        
        

def rulematch():
    # rulefilename = "/media/vezir/b2552981-cae5-4a83-9f27-2d07beede43e/CRYPTOREX/rex/misuseprofile"
    rulefilename = config.misuseprofile_path
    print(rulefilename)
    rulefd = open(rulefilename,"r")
    print(f'rulefd')
    #print(rulefd)
    print("----------------")
    funcnameset = set()
    funcdetail = dict()
    wfuncdetail = dict()
    ruledesresult = dict()
    wfuncset=set()
    ruledesflag = False
    misusefunctionflag = False
    dependflag = False
    while True:
        line = rulefd.readline().strip()
        if not line:
            break
        if line == "ruledes:":
            ruledesflag = True
            misusefunctionflag = False
            wrongflag = False
        elif line == "misusefunction:":
            ruledesflag = False
            misusefunctionflag = True
            wrongflag = False
        elif line == "dependfunc:":
            wrongflag = True
            ruledesflag = False
            dependflag = False

        if misusefunctionflag:
            if not len(line) == 0 and line[0] == "#":
                continue
            field = line.split("\t")
            if not len(field) == 2:
                continue
            funcprototype = re.split("[(),]",field[0].strip())
            if len(funcprototype) == 0:
                continue
            funcheader = funcprototype[0].split(" ")
            if not len(funcheader) == 2:
                continue
            if funcheader[1][0] == "*":
                funcheader[1] = funcheader[1][1:len(funcheader[1])]
                funcheader[0] += "*"
            funcnameset.add(funcheader[1])
            tmpfunction=function()
            tmpfunction.setfunctionname(funcheader[1])
            tmpfunction.setreturntype(funcheader[0])
            for i in range(1,len(funcprototype)):
                if funcprototype[i] == "":
                    continue
                tmpfunction.addarg(funcprototype[i].strip())
            farglocat = field[1].split(";")
            for glocatg in farglocat:
                glocat = glocatg.split(":")
                if not len(glocat) == 4:
                    continue
                if glocat[1].strip() == "string":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vstring])
                elif glocat[1].strip() == "int":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vint])
                elif glocat[1].strip() == "len":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vlen])
                elif glocat[1].strip() == "none":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vnone])
                tmpfunction.addrule(int(glocat[2]))
                tmpfunction.addruledes(ruledesresult[int(glocat[2])])
                tmpfunction.addlimit(glocat[3])
            tmpfunction.listallfagrpp()
            funcdetail[funcheader[1]] = tmpfunction
        elif ruledesflag:
            if not len(line) == 0 and line[0] == "#":
                continue
            field = line.split("\t")
            if not len(field) == 2:
                continue
            ruledesresult[int(field[0])] = field[1]
        elif dependflag:
            if not len(line) == 0 and line[0] == "#":
                continue
            functionfield = line.split("->")
            if not len(field) == 2:
                continue
            funcprototype = re.split("[(),]",field[0].strip())
            if len(funcprototype) == 0:
                continue
            funcheader = funcprototype[0].split(" ")
            if not len(funcheader) == 2:
                continue
            if funcheader[1][0] == "*":
                funcheader[1] = funcheader[1][1:len(funcheader[1])]
                funcheader[0] += "*"
            wfuncset.add(funcheader[1])
            tmpfunction=function()
            tmpfunction.setfunctionname(funcheader[1])
            tmpfunction.setreturntype(funcheader[0])
            for i in range(1,len(funcprototype)):
                if funcprototype[i] == "":
                    continue
                tmpfunction.addarg(funcprototype[i].strip())
            farglocat = field[1].split("")
            for glocatg in farglocat:
                glocat = glocatg.split(":")
                if not len(glocat) == 4:
                    continue
                if glocat[1].strip() == "string":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vstring])
                elif glocat[1].strip() == "int":
                    tmpfunction.addfarg([int(glocat[0]),FARGTYPE.Vint])
                tmpfunction.addrule(int(glocat[2]))
                tmpfunction.addruledes(ruledesresult[int(glocat[2])])
                tmpfunction.addlimit(glocat[3])
            wfuncdetail[funcheader[1]] = tmpfunction
            
    rulefd.close()
    return funcnameset,funcdetail,ruledesresult,wfuncset,wfuncdetail

'''def finishfuncdetail(function,pnode):
    function.clearfunctionaarg()
    if len(function.getarg()) < 4:
        comlist = pnode.getcomarglist()
        for i in range(0,len(function.getarg())):
            function.addfunctionaarg([comlist[i],ARGTYPE.Voffset])
    else:
        aargnum = len(function.getarg())
        comlist = pnode.getcomarglist()
        for i in range(0,4):
            function.addfunctionaarg([comlist[i],ARGTYPE.Voffset])
        for i in range(4,aargnum):
            function.addfunctionaarg([i-4,ARGTYPE.Vstackv])
'''		
    
def reversedfs(node,time,prefix=""):
    msg = prefix
    msg += node.getmetadata() + " "
    for pnode in node.getparents():
        reversedfs(pnode[0],time+1,msg)
    if len(node.getparents()) == 0:
        print(msg)


archdataformat = ["word_","dword_","unk_","byte_"]

def hex2str(hexstr):
    datad = hexstr
    fdata = ""
    if datad.lower().startswith("0x"):
        dfield = datad.split(",")
        for fditem in dfield:
            tmpdata = fditem.strip()
            if tmpdata.lower().startswith("0x"):
                tmpdata = tmpdata[2:]
                if len(tmpdata) % 2 == 1:
                    tmpdata = "0" + tmpdata
                fdata += binascii.a2b_hex(tmpdata)[::-1].decode('utf-8')
            else:
                fdata = datad
    else:
        fdata = hexstr
    return fdata

# ???
def reversetracedfs(nodeset,tinfo,offset,alldata,soffset,depth,execfuncdetail,allfn,middlefunc,ef,detailreport,wfuncsetreturn,pathroad, call_stack=list(), proj: angr.Project=None):
    # node.stack[tinfo.vl[indexvt] + soffset][1] == ARGTYPE.Vtmp
    # dbg(f'''
    # 	==================reversetracedfs================
    # 	nodeset: {nodeset}
    # 	tinfo: {tinfo}
    # 	offset: {offset}
    # 	soffset: {soffset}
    # 	depth: {depth}
    # 	execfunctiondetial: {execfuncdetail}
    # 	allfn: {allfn}
    # 	middlefunc: {middlefunc}
    # 	ef: {ef}
    # 	detailreport: {detailreport}
    # 	wfuncsetreturn: {wfuncsetreturn}
    # 	pathroad: {pathroad}
    # 	===================================================
    # ''')
    node = nodeset[0]	# parent problock
    irsb = node.getirsb()
    takeaction = False
    actionv = list()
    actiont = list()
    ntinfo = traceinfo()
    slidechild = nodeset[1]	# jumpkind
    childlocat = nodeset[2]
    '''msg = ""
    for i in range(0,time):
        msg +=" "
    msg += "0x%X"%node.beginaddr
    print(msg)'''
    global starttime
    nowtime = time.time()
    #print(int(nowtime-starttime))
    if int(nowtime - starttime)/60 >= 2:
        return
    if node.beginaddr == 0x107bc:
        print("???")
    if node.beginaddr in pathroad:
        return
    else:
        pathroad.append(node.beginaddr)
        if node.beginaddr in proj.kb.functions:
            func = proj.kb.functions[node.beginaddr]
            call_stack.append(f'{func.name} ({hex(func.addr)})')
    print(f"DEBUG-1: {list(map(hex, pathroad))}")
    print(f"DEBUG-2: {childlocat}")
    for indexi in range(0,childlocat):
        if slidechild == CHILRENSLIDE.Vleft:
            childpro = node.getleftchildren()[indexi]
            # fix-up for taint transfer
            if childpro.externflag() and childpro.getexternfun() in execfuncdetail:
                execfunname = childpro.getexternfun()
                src = execfuncdetail[execfunname].getfuncsrc() - 1
                dest = execfuncdetail[execfunname].getfuncdest() - 1
                destv = 0
                destvtype = 0
                if dest < 4:
                    destv = node.getcomarglist()[dest]
                    destvtype = ARGTYPE.Voffset
                    meta = ""
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.addalllist(destv,destvtype,meta,vargtype,node.beginaddr,-1,"")
                else:
                    destv = dest - 4
                    destvtype = ARGTYPE.Vstackv
                    meta = ""
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.addalllist(destv,destvtype,meta,vargtype,node.beginaddr,-1,"")
                if src < 4:
                    v = node.getcomarglist()[src]
                    vtype = ARGTYPE.Voffset
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.keyadddup(destv,destvtype,v,vtype)
                else:
                    v = src - 4
                    vtype = ARGTYPE.Vstackv
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.keyadddup(destv,destvtype,v,vtype)
            elif childpro.externflag():
                for index in range(0,node.unfixedarglen()):
                    offset = node.getunfixedarg(index)
                    # tinfo belongs to its successive block (maybe an extern function's entry)
                    if tinfo.keyin(offset,ARGTYPE.Voffset):
                        tinfo.setntrace(offset,ARGTYPE.Voffset)
            #if childpro.externflag() and childpro.getexternfun() in wfuncsetreturn:
            #	print(childpro.getexternfun())
            
        elif slidechild == CHILRENSLIDE.Vright:
            childpro = node.getrightchildren()[indexi]
            # ?
            # duplicated code
            if childpro.externflag() and childpro.getexternfun() in execfuncdetail:
                execfunname = childpro.getexternfun()
                src = execfuncdetail[execfunname].getfuncsrc() - 1
                dest = execfuncdetail[execfunname].getfuncdest() - 1
                destv = 0
                destvtype = 0
                if dest < 4:
                    destv = node.getcomarglist()[dest]
                    destvtype = ARGTYPE.Voffset
                    meta = ""
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.addalllist(destv,destvtype,meta,vargtype,node.beginaddr,-1,"")
                else:
                    destv = dest - 4
                    destvtype = ARGTYPE.Vstackv
                    meta = ""
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.addalllist(destv,destvtype,meta,vargtype,node.beginaddr,-1,"")
                if src < 4:
                    v = node.getcomarglist()[src]
                    vtype = ARGTYPE.Voffset
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.keyadddup(destv,destvtype,v,vtype)
                else:
                    v = src - 4
                    vtype = ARGTYPE.Vstackv
                    vargtype = execfuncdetail[execfunname].getsrctype()
                    ntinfo.keyadddup(destv,destvtype,v,vtype)
            elif childpro.externflag():
                for index in range(0,node.unfixedarglen()):
                    offset = node.getunfixedarg(index)
                    if tinfo.keyin(offset,ARGTYPE.Voffset):
                        tinfo.setntrace(offset,ARGTYPE.Voffset)
    for indexvt in range(0,len(tinfo.vtypel)):
        if not tinfo.vtypel[indexvt] == ARGTYPE.Vstackv:
            continue
        elif tinfo.vl[indexvt]+soffset < 0:
            tinfo.setntrace(tinfo.vl[indexvt],tinfo.vtypel[indexvt])
        elif tinfo.vl[indexvt] + soffset >= len(node.stack):
            continue
        elif node.stack[tinfo.vl[indexvt] + soffset][1] == ARGTYPE.Vtmp:
            if str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1]) in node.sprelate:
                for spitem in node.sprelate:
                    if node.sprelate[str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1])] == node.sprelate[spitem] and not str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1]) == spitem:
                        field = spitem.split(" ")
                        tinfo.keyadddup(tinfo.vl[indexvt],tinfo.vtypel[indexvt],int(field[0]),field[1])
            tinfo.keyupdate(tinfo.vl[indexvt],tinfo.vtypel[indexvt],node.stack[tinfo.vl[indexvt] + soffset][0],node.stack[tinfo.vl[indexvt] + soffset][1])
        elif node.stack[tinfo.vl[indexvt] + soffset][1] == ARGTYPE.Vconst:
            if tinfo.getargtype(tinfo.vl[indexvt],tinfo.vtypel[indexvt]) == FARGTYPE.Vint:
                tinfo.setfresult(tinfo.vl[indexvt],tinfo.vtypel[indexvt],node.stack[tinfo.vl[indexvt] + soffset][0])
                tinfo.setntrace(tinfo.vl[indexvt],tinfo.vtypel[indexvt])
            elif tinfo.getargtype(tinfo.vl[indexvt],tinfo.vtypel[indexvt]) == FARGTYPE.Vstring:
                if node.stack[tinfo.vl[indexvt] + soffset][0] in alldata and isinstance(alldata[node.stack[tinfo.vl[indexvt] + soffset][0]],int) and alldata[node.stack[tinfo.vl[indexvt] + soffset][0]] in alldata:	
                    fresult = hex2str(alldata[alldata[node.stack[tinfo.vl[indexvt] + soffset][0]]])
                    tinfo.setfresult(tinfo.vl[indexvt],tinfo.vtypel[indexvt],fresult)
                    tinfo.setntrace(tinfo.vl[indexvt],tinfo.vtypel[indexvt])
                elif node.stack[tinfo.vl[indexvt] + soffset][0] in alldata and not isinstance(alldata[node.stack[tinfo.vl[indexvt] + soffset][0]],int):
                    fresult = hex2str(alldata[node.stack[tinfo.vl[indexvt] + soffset][0]])
                    tinfo.setfresult(tinfo.vl[indexvt],tinfo.vtypel[indexvt],fresult)
                    tinfo.setntrace(tinfo.vl[indexvt],tinfo.vtypel[indexvt])
                else:
                    tinfo.keyupdate(tinfo.vl[indexvt],tinfo.vtypel[indexvt],node.stack[tinfo.vl[indexvt] + soffset][0],node.stack[tinfo.vl[indexvt] + soffset][1])
        elif node.stack[tinfo.vl[indexvt] + soffset][1] == ARGTYPE.Voffset:
            if str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1]) in node.sprelate:
                for spitem in node.sprelate:
                    if node.sprelate[str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1])] == node.sprelate[spitem] and not str(node.stack[tinfo.vl[indexvt] + soffset][0]) + " " + str(node.stack[tinfo.vl[indexvt] + soffset][1]) == spitem:
                        field = spitem.split(" ")
                        tinfo.keyadddup(tinfo.vl[indexvt],tinfo.vtypel[indexvt],int(field[0]),field[1])
            tinfo.keyupdate(tinfo.vl[indexvt],tinfo.vtypel[indexvt],node.stack[tinfo.vl[indexvt] + soffset][0],node.stack[tinfo.vl[indexvt] + soffset][1])
    #if node.beginaddr == 0x4008d8 or node.beginaddr == 0x10550:
    #	print("bbegin0x%X"%node.beginaddr)
    #	tinfo.listdebugpp()
    #	print(node.stack)
    #	print(node.sprelate)
    if not ntinfo.ntlen() == 0:
        for sitem in reversed(irsb.statements):
            if sitem.tag == "Ist_IMark":
                if takeaction:
                    takeaction = False
                    for i in range(0,len(actionv)):
                        ntinfo.setfaddr(actionv[i],actiont[i],sitem.addr)
                        comment = ""
                        dataaddr = 0x0
                        if not ntinfo.gettrace(actionv[i],actiont[i]):
                            continue
                        if sitem.addr in node.lcom:
                            comment = node.lcom[sitem.addr]
                        else:
                            continue
                        #print(comment)
                        if ntinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring and comment[0] == "\"" and comment[len(comment) - 1] == "\"":
                            ntinfo.setfresult(actionv[i],actiont[i],node.lcom[sitem.addr])
                            ntinfo.setntrace(actionv[i],actiont[i])
                        elif ntinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring and comment[0] == "\'" and comment[len(comment) - 1] == "\'":
                            ntinfo.setfresult(actionv[i],actiont[i],node.lcom[sitem.addr])
                            ntinfo.setntrace(actionv[i],actiont[i])
                        elif ntinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring:
                            for dfitem in archdataformat:
                                if comment.lower().startswith(dfitem):
                                    dataaddr = int(comment.lower()[len(dfitem):len(comment)],16) + offset
                                    if dataaddr in alldata:
                                        nprint = True
                                        datad = alldata[dataaddr]
                                        fdata = hex2str(datad)
                                        ntinfo.setfresult(actionv[i],actiont[i],fdata)
                                        ntinfo.setntrace(actionv[i],actiont[i])
                                        break
                            #ntinfo.setntrace(actionv[i],actiont[i])
                actionv = []
                actiont = []
            elif sitem.tag == "Ist_Exit":
                continue
            elif sitem.tag == "Ist_Put":
                if ntinfo.keyin(sitem.offset,ARGTYPE.Voffset) and ntinfo.gettrace(sitem.offset,ARGTYPE.Voffset):
                    eitem = sitem.data
                    if eitem.tag == "Iex_Unop":
                        pass
                    elif eitem.tag == "Iex_RdTmp":
                        takeaction = True
                        ntinfo.keyupdate(sitem.offset,ARGTYPE.Voffset,eitem.tmp,ARGTYPE.Vtmp)
                        actionv.append(eitem.tmp)
                        actiont.append(ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Load":
                        pass
                    elif eitem.tag == "Iex_Const":
                        if ntinfo.getargtype(sitem.offset,ARGTYPE.Voffset) == FARGTYPE.Vint:
                            takeaction = True
                            ntinfo.setfresult(sitem.offset,ARGTYPE.Voffset,eitem.con.value)
                            ntinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                            actionv.append(sitem.offset)
                            actiont.append(ARGTYPE.Voffset)
                        elif ntinfo.getargtype(sitem.offset,ARGTYPE.Voffset) == FARGTYPE.Vstring:
                            takeaction = True
                            if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                fresult = hex2str(alldata[alldata[eitem.con.value]])
                                ntinfo.setfresult(sitem.offset,ARGTYPE.Voffset,fresult)
                                ntinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                                takeaction = True
                            elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                fresult = hex2str(alldata[eitem.con.value])
                                ntinfo.setfresult(sitem.offset,ARGTYPE.Voffset,fresult)
                                ntinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                                takeaction = True
                            else:
                                takeaction = True
                                ntinfo.setfresult(sitem.offset,ARGTYPE.Voffset,eitem.con.value)
                                ntinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                                actionv.append(sitem.offset)
                                actiont.append(ARGTYPE.Voffset)
                    elif eitem.tag == "Iex_Binop":
                        pass
                    elif eitem.tag == "Iex_Get":
                        pass
            elif sitem.tag == "Ist_WrTmp":
                if ntinfo.keyin(sitem.tmp,ARGTYPE.Vtmp) and ntinfo.gettrace(sitem.tmp,ARGTYPE.Vtmp):
                    eitem = sitem.data
                    if eitem.tag == "Iex_Unop":
                        pass
                    elif eitem.tag == "Iex_RdTmp":
                        ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Load":
                        laddr = eitem.addr
                        if ntinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vstring:
                            if laddr.tag == "Iex_Const" and laddr.con.value in alldata and isinstance(alldata[laddr.con.value],int)and alldata[laddr.con.value] in alldata:	
                                fresult = hex2str(alldata[alldata[laddr.con.value]])
                                ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif laddr.tag == "Iex_Const" and laddr.con.value in alldata and not isinstance(alldata[laddr.con.value],int):
                                fresult = hex2str(alldata[laddr.con.value])
                                ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif laddr.tag == "Iex_RdTmp" and ntinfo.gettrace(sitem.tmp,ARGTYPE.Vtmp):
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(laddr.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(laddr.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                        ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                        ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,laddr.tmp,ARGTYPE.Vtmp)
                                    actionv.append(laddr.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                        elif ntinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                            if laddr.tag == "Iex_Const":
                                ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,laddr.con.value)
                                ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                            elif laddr.tag == "Iex_RdTmp" and node.instack(laddr.tmp,ARGTYPE.Vtmp):
                                takeaction = True
                                stacklocatinfo = node.getstackdata(laddr.tmp ,ARGTYPE.Vtmp)
                                v = stacklocatinfo[0]
                                vtype = stacklocatinfo[1]
                                if vtype == ARGTYPE.Voffset:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Voffset)
                                elif vtype == ARGTYPE.Vtmp:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Vtmp)
                                elif vtype == ARGTYPE.Vconst:
                                    ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,v)
                                    ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                            elif laddr.tag == "Iex_RdTmp":
                                ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,laddr.tmp,ARGTYPE.Vtmp)
                        elif eitem.tag == "Iex_Const":
                            if ntinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                                takeaction = True
                                ntinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,eitem.con.value)
                                ntinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                actionv.append(sitem.tmp)
                                actiont.append(ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Binop":
                        takeaction = True
                    elif eitem.tag == "Iex_Get":
                        takeaction = True
                        ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,eitem.offset,ARGTYPE.Voffset)
                        actionv.append(eitem.offset)
                        actiont.append(ARGTYPE.Voffset)
            elif sitem.tag == "Ist_Store":
                if sitem.addr.tag == "Iex_Const":
                    if ntinfo.keyin(sitem.addr.constants[0].value,ARGTYPE.Vconst) and ntinfo.gettrace(sitem.addr.constants[0].value,ARGTYPE.Vconst):
                        eitem = sitem.data
                        if eitem.tag == "Iex_Const":
                            if ntinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vint:
                                ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.con.value)
                                ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                takeaction = True
                            elif ntinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vstring:
                                if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                    fresult = hex2str(alldata[alldata[eitem.con.value]])
                                    ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                    ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                    takeaction = True
                                elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                    fresult = hex2str(alldata[eitem.con.value])
                                    ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                    ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                    takeaction = True
                                else:
                                    ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.con.value,ARGTYPE.Vconst)
                                    actionv.append(eitem.con.value)
                                    actiont.append(ARGTYPE.Vconst)
                                    takeaction = True
                        elif eitem.tag == "Iex_RdTmp":
                            if ntinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vint:
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    takeaction = True
                                    stacklocatinfo = node.getstackdata(eitem.tmp ,ARGTYPE.Vtmp)
                                    v = stacklocatinfo[0]
                                    vtype = stacklocatinfo[1]
                                    if vtype == ARGTYPE.Voffset:
                                        ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,ARGTYPE.Voffset)
                                    elif vtype == ARGTYPE.Vtmp:
                                        ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,ARGTYPE.Vtmp)
                                    elif vtype == ARGTYPE.Vconst:
                                        ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,v)
                                        ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                            elif ntinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vstring:
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(eitem.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                        ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        ntinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                        ntinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    ntinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.tmp,ARGTYPE.Vtmp)
                                    actionv.append(eitem.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                                    takeaction = True
                elif sitem.addr.tag == "Iex_RdTmp":
                    if ntinfo.keyin(sitem.addr.tmp,ARGTYPE.Vtmp) and ntinfo.gettrace(sitem.addr.tmp,ARGTYPE.Vtmp):
                        eitem = sitem.data
                        if eitem.tag == "Iex_Const":
                            if ntinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp,ARGTYPE.Vconst) == FARGTYPE.Vint:
                                ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.con.value)
                                ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif ntinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp,ARGTYPE.Vconst) == FARGTYPE.Vstring:
                                if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                    fresult = hex2str(alldata[alldata[eitem.con.value]])
                                    ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                    ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp,ARGTYPE.Vconst)
                                    takeaction = True
                                elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                    fresult = hex2str(alldata[eitem.con.value])
                                    ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                    ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                    takeaction = True
                                else:
                                    ntinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.con.value,ARGTYPE.Vconst)
                                    actionv.append(eitem.con.value)
                                    actiont.append(ARGTYPE.Vconst)
                                    takeaction = True
                        elif eitem.tag == "Iex_RdTmp":
                            if ntinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    takeaction = True
                                    stacklocatinfo = node.getstackdata(eitem.tmp ,ARGTYPE.Vtmp)
                                    v = stacklocatinfo[0]
                                    vtype = stacklocatinfo[1]
                                    if vtype == ARGTYPE.Voffset:
                                        ntinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Voffset)
                                    elif vtype == ARGTYPE.Vtmp:
                                        ntinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Vtmp)
                                    elif vtype == ARGTYPE.Vconst:
                                        ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,v)
                                        ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                            elif ntinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vstring:
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(eitem.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    ntinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                        ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        ntinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                        ntinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    ntinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                                    actionv.append(eitem.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                            ntinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                            actionv.append(eitem.tmp)
                            actiont.append(ARGTYPE.Vtmp)
                            takeaction = True
    #if node.beginaddr == 0x402dd8 or node.beginaddr == 0x10550:
    #	print("vbegin0x%X"%node.beginaddr)
    #	tinfo.listdebugpp()
    #	print(node.stack)
    #	print(node.sprelate)
    for i in range(0,tinfo.alllen()):
        vv = tinfo.getindexvl(i)
        vtypev = tinfo.getindexvtypel(i)
        if ntinfo.keyin(vv,vtypev) and not ntinfo.gettrace(vv,vtypev):
            tinfo.setfresult(vv,vtypev,ntinfo.getfresult(vv,vtypev))
            tinfo.setfaddr(vv,vtypev,ntinfo.getfaddr(vv,vtypev))
            tinfo.setntrace(vv,vtypev)
    if not tinfo.ntlen() == 0:
        for sitem in reversed(irsb.statements):
            if sitem.tag == "Ist_IMark":
                #print(takeaction)
                if takeaction:
                    #print("0x%X"%sitem.addr)
                    #print(actionv)
                    #print(actiont)
                    takeaction = False
                    for i in range(0,len(actionv)):
                        tinfo.setfaddr(actionv[i],actiont[i],sitem.addr)
                        comment = ""
                        dataaddr = 0x0
                        if not tinfo.gettrace(actionv[i],actiont[i]):
                            continue
                        if sitem.addr in node.lcom:
                            comment = node.lcom[sitem.addr]
                        else:
                            continue
                        #print(comment)
                        if tinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring and comment[0] == "\"" and comment[len(comment) - 1] == "\"":
                            tinfo.setfresult(actionv[i],actiont[i],node.lcom[sitem.addr])
                            tinfo.setntrace(actionv[i],actiont[i])
                        elif tinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring and comment[0] == "\'" and comment[len(comment) - 1] == "\'":
                            tinfo.setfresult(actionv[i],actiont[i],node.lcom[sitem.addr])
                            tinfo.setntrace(actionv[i],actiont[i])
                        elif tinfo.getargtype(actionv[i],actiont[i]) == FARGTYPE.Vstring:
                            for dfitem in archdataformat:
                                if comment.lower().startswith(dfitem):
                                    dataaddr = int(comment.lower()[len(dfitem):len(comment)],16) + offset
                                    if dataaddr in alldata:
                                        nprint = True
                                        datad = alldata[dataaddr]
                                        fdata = hex2str(datad)
                                        tinfo.setfresult(actionv[i],actiont[i],fdata)
                                        tinfo.setntrace(actionv[i],actiont[i])
                                        break
                            #tinfo.setntrace(actionv[i],actiont[i])
                actionv = []
                actiont = []
            elif sitem.tag == "Ist_Exit":
                continue
            elif sitem.tag == "Ist_Put":
                if tinfo.keyin(sitem.offset,ARGTYPE.Voffset) and tinfo.gettrace(sitem.offset,ARGTYPE.Voffset):
                    eitem = sitem.data
                    if eitem.tag == "Iex_Unop":
                        pass
                    elif eitem.tag == "Iex_RdTmp":
                        takeaction = True
                        tinfo.keyupdate(sitem.offset,ARGTYPE.Voffset,eitem.tmp,ARGTYPE.Vtmp)
                        actionv.append(eitem.tmp)
                        actiont.append(ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Load":
                        pass
                    elif eitem.tag == "Iex_Const":
                        if tinfo.getargtype(sitem.offset,ARGTYPE.Voffset) == FARGTYPE.Vint:
                            takeaction = True
                            tinfo.setfresult(sitem.offset,ARGTYPE.Voffset,eitem.con.value)
                            tinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                            actionv.append(sitem.offset)
                            actiont.append(ARGTYPE.Voffset)
                        elif tinfo.getargtype(sitem.offset,ARGTYPE.Voffset) == FARGTYPE.Vstring:
                            takeaction = True
                            if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                fresult = hex2str(alldata[alldata[eitem.con.value]])
                                tinfo.setfresult(sitem.offset,ARGTYPE.Voffset,fresult)
                                tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                fresult = hex2str(alldata[eitem.con.value])
                                tinfo.setfresult(sitem.offset,ARGTYPE.Voffset,fresult)
                                tinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                                takeaction = True
                            else:
                                takeaction = True
                                tinfo.setfresult(sitem.offset,ARGTYPE.Voffset,eitem.con.value)
                                tinfo.setntrace(sitem.offset,ARGTYPE.Voffset)
                                actionv.append(sitem.offset)
                                actiont.append(ARGTYPE.Voffset)
                    elif eitem.tag == "Iex_Binop":
                        pass
                    elif eitem.tag == "Iex_Get":
                        pass
            elif sitem.tag == "Ist_WrTmp":
                if tinfo.keyin(sitem.tmp,ARGTYPE.Vtmp) and tinfo.gettrace(sitem.tmp,ARGTYPE.Vtmp):
                    eitem = sitem.data
                    if eitem.tag == "Iex_Unop":
                        pass
                    elif eitem.tag == "Iex_RdTmp":
                        tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Load":
                        laddr = eitem.addr
                        if tinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vstring:
                            if laddr.tag == "Iex_Const" and laddr.con.value in alldata and isinstance(alldata[laddr.con.value],int)and alldata[laddr.con.value] in alldata:	
                                # if node.beginaddr == 0x105B4:
                                #     print(f'DEBUG: {alldata[laddr.con.value]}')
                                #     print(f'DEBUG: {alldata[alldata[laddr.con.value]]}')
                                # [!!!] 
                                fresult = hex2str(alldata[alldata[laddr.con.value]])
                                tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif laddr.tag == "Iex_Const" and laddr.con.value in alldata and not isinstance(alldata[laddr.con.value],int):
                                fresult = hex2str(alldata[laddr.con.value])
                                tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif laddr.tag == "Iex_RdTmp" and tinfo.gettrace(sitem.tmp,ARGTYPE.Vtmp):
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(laddr.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(laddr.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                        tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,fresult)
                                        tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,laddr.tmp,ARGTYPE.Vtmp)
                                    actionv.append(laddr.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                        elif tinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                            if laddr.tag == "Iex_Const":
                                tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,laddr.con.value)
                                tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                            elif laddr.tag == "Iex_RdTmp" and node.instack(laddr.tmp,ARGTYPE.Vtmp):
                                takeaction = True
                                stacklocatinfo = node.getstackdata(laddr.tmp ,ARGTYPE.Vtmp)
                                v = stacklocatinfo[0]
                                vtype = stacklocatinfo[1]
                                #print(vtype)
                                if vtype == ARGTYPE.Voffset:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Voffset)
                                elif vtype == ARGTYPE.Vtmp:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Vtmp)
                                elif vtype == ARGTYPE.Vconst:
                                    tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,v)
                                    tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                elif vtype == ARGTYPE.Vunkown:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,laddr.tmp,ARGTYPE.Vtmp)
                                    actionv.append(laddr.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                            elif laddr.tag == "Iex_RdTmp":
                                tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,laddr.tmp,ARGTYPE.Vtmp)
                            
                        elif eitem.tag == "Iex_Const":
                            if tinfo.getargtype(sitem.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                                takeaction = True
                                tinfo.setfresult(sitem.tmp,ARGTYPE.Vtmp,eitem.con.value)
                                tinfo.setntrace(sitem.tmp,ARGTYPE.Vtmp)
                                actionv.append(sitem.tmp)
                                actiont.append(ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Binop":
                        takeaction = True
                        actionv.append(sitem.tmp)
                        actiont.append(ARGTYPE.Vtmp)
                    elif eitem.tag == "Iex_Get":
                        takeaction = True
                        tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,eitem.offset,ARGTYPE.Voffset)
                        actionv.append(eitem.offset)
                        actiont.append(ARGTYPE.Voffset)
            elif sitem.tag == "Ist_Store":
                if sitem.addr.tag == "Iex_Const":
                    if tinfo.keyin(sitem.addr.constants[0].value,ARGTYPE.Vconst) and tinfo.gettrace(sitem.addr.constants[0].value,ARGTYPE.Vconst):
                        eitem = sitem.data
                        if eitem.tag == "Iex_Const":
                            if tinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vint:
                                tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.con.value)
                                tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                takeaction = True
                            elif tinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vstring:
                                if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                    fresult = hex2str(alldata[alldata[eitem.con.value]])
                                    tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                    tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                    takeaction = True
                                elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                    fresult = hex2str(alldata[eitem.con.value])
                                    tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                    tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                    takeaction = True
                                else:
                                    tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.con.value,ARGTYPE.Vconst)
                                    actionv.append(eitem.con.value)
                                    actiont.append(ARGTYPE.Vconst)
                                    takeaction = True
                        elif eitem.tag == "Iex_RdTmp":
                            if tinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vint:
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    takeaction = True
                                    stacklocatinfo = node.getstackdata(eitem.tmp ,ARGTYPE.Vtmp)
                                    v = stacklocatinfo[0]
                                    vtype = stacklocatinfo[1]
                                    if vtype == ARGTYPE.Voffset:
                                        tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,ARGTYPE.Voffset)
                                    elif vtype == ARGTYPE.Vtmp:
                                        tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,ARGTYPE.Vtmp)
                                    elif vtype == ARGTYPE.Vconst:
                                        tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,v)
                                        tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                            elif tinfo.getargtype(sitem.addr.constants[0].value,ARGTYPE.Vconst) == FARGTYPE.Vstring:
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(eitem.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                        tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        tinfo.setfresult(sitem.addr.constants[0].value,ARGTYPE.Vconst,fresult)
                                        tinfo.setntrace(sitem.addr.constants[0].value,ARGTYPE.Vconst)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    tinfo.keyupdate(sitem.addr.constants[0].value,ARGTYPE.Vconst,eitem.tmp,ARGTYPE.Vtmp)
                                    actionv.append(eitem.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                                    takeaction = True
                elif sitem.addr.tag == "Iex_RdTmp":
                    if tinfo.keyin(sitem.addr.tmp,ARGTYPE.Vtmp) and tinfo.gettrace(sitem.addr.tmp,ARGTYPE.Vtmp):
                        eitem = sitem.data
                        if eitem.tag == "Iex_Const":
                            if tinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                                tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.con.value)
                                tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                takeaction = True
                            elif tinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vstring:
                                if eitem.con.value in alldata and isinstance(alldata[eitem.con.value],int)and alldata[eitem.con.value] in alldata:	
                                    fresult = hex2str(alldata[alldata[eitem.con.value]])
                                    tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                    tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp,ARGTYPE.Vconst)
                                    takeaction = True
                                elif eitem.con.value in alldata and not isinstance(alldata[eitem.con.value],int):
                                    fresult = hex2str(alldata[eitem.con.value])
                                    tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                    tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                    takeaction = True
                                else:
                                    tinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.con.value,ARGTYPE.Vconst)
                                    actionv.append(eitem.con.value)
                                    actiont.append(ARGTYPE.Vconst)
                                    takeaction = True
                        elif eitem.tag == "Iex_RdTmp":
                            if tinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vint:
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    takeaction = True
                                    stacklocatinfo = node.getstackdata(eitem.tmp ,ARGTYPE.Vtmp)
                                    v = stacklocatinfo[0]
                                    vtype = stacklocatinfo[1]
                                    if vtype == ARGTYPE.Voffset:
                                        tinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Voffset)
                                    elif vtype == ARGTYPE.Vtmp:
                                        tinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,v,ARGTYPE.Vtmp)
                                    elif vtype == ARGTYPE.Vconst:
                                        tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,v)
                                        tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                            elif tinfo.getargtype(sitem.addr.tmp,ARGTYPE.Vtmp) == FARGTYPE.Vstring:
                                v = 0
                                vtype = ARGTYPE.Vunkown
                                if node.instack(eitem.tmp,ARGTYPE.Vtmp):
                                    tmpvstackdata = node.getstackdata(eitem.tmp,ARGTYPE.Vtmp)
                                    v = tmpvstackdata[0]
                                    vtype = tmpvstackdata[1]
                                if vtype == ARGTYPE.Voffset:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vtmp:
                                    tinfo.keyupdate(sitem.tmp,ARGTYPE.Vtmp,v,vtype)
                                elif vtype == ARGTYPE.Vconst:
                                    if v in alldata and isinstance(alldata[v],int)and alldata[v] in alldata:	
                                        fresult = hex2str(alldata[alldata[v]])
                                        tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                        tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                    elif v in alldata and not isinstance(alldata[v],int):
                                        fresult = hex2str(alldata[laddr.con.value])
                                        tinfo.setfresult(sitem.addr.tmp,ARGTYPE.Vtmp,fresult)
                                        tinfo.setntrace(sitem.addr.tmp,ARGTYPE.Vtmp)
                                        takeaction = True
                                elif vtype == ARGTYPE.Vunkown:
                                    tinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                                    actionv.append(eitem.tmp)
                                    actiont.append(ARGTYPE.Vtmp)
                            tinfo.keyupdate(sitem.addr.tmp,ARGTYPE.Vtmp,eitem.tmp,ARGTYPE.Vtmp)
                            actionv.append(eitem.tmp)
                            actiont.append(ARGTYPE.Vtmp)
                            takeaction = True
    #if node.beginaddr == 0x402dd8 or node.beginaddr == 0x10550:
    #	print("middle0x%X"%node.beginaddr)
    #	tinfo.listdebugpp()
    #	print(node.stack)
    #	print(node.sprelate)
    for i in range(0,tinfo.alllen()):
        vv = tinfo.getindexvl(i)
        vtypev = tinfo.getindexvtypel(i)
        if ntinfo.keyin(vv,vtypev) and not ntinfo.gettrace(vv,vtypev):
            tinfo.setfresult(vv,vtypev,ntinfo.getfresult(vv,vtypev))
            tinfo.setfaddr(vv,vtypev,ntinfo.getfaddr(vv,vtypev))
            tinfo.setntrace(vv,vtypev)
    for i in range(0,len(tinfo.vtypel)):
        if tinfo.vtypel[i] == ARGTYPE.Vconst:
            v = tinfo.vl[i]
            if v in alldata:
                tinfo.setfresult(v,tinfo.vtypel[i],alldata[v])
                tinfo.setntrace(v,tinfo.vtypel[i])
    for indexvt in range(0,len(tinfo.vtypel)):
        if not tinfo.vtypel[indexvt] == ARGTYPE.Vtmp:
            continue
        elif not (tinfo.keyin(tinfo.vl[indexvt],tinfo.vtypel[indexvt]) and tinfo.gettrace(tinfo.vl[indexvt],tinfo.vtypel[indexvt])):
            continue
        elif not str(tinfo.vl[indexvt]) + " " + str(tinfo.vtypel[indexvt]) in node.sprelate:
            continue
        else:
            tinfo.keyupdate(tinfo.vl[indexvt],tinfo.vtypel[indexvt],node.sprelate[str(tinfo.vl[indexvt]) + " " + str(tinfo.vtypel[indexvt])]/node.getwordlen() + node.stackfixnum,ARGTYPE.Vstackv)
    #if node.beginaddr == 0x402dd8 or node.beginaddr == 0x10550:
    #	print("end0x%X"%node.beginaddr)
    #	tinfo.listdebugpp()
    #	print(node.stack)
    #	print(node.sprelate)
    tinfo.listallpp(proj.filename, call_stack, pathroad, detailreport)
    tinfo.settntrace()
    if node.beginaddr in allfn:
        dfun = traceinfo2func(tinfo,node,allfn[node.beginaddr])
        if dfun.getfunctionname() in ef:
            middlefunc[dfun.getfunctionname()] = dfun
    print(f'DEBUG-444: {hex(node.beginaddr)}')
    print(f'DEBUG-44: {tinfo.ntlen()}')
    print(f'DEBUG-4: {node.getparents()}')
    if tinfo.ntlen() == 0:
        return
    for pitem in node.getparents():
        print(f'DEBUG-3: {pitem}')
        reversetracedfs(pitem,traceinfocopy(tinfo),offset,alldata,node.stackoffset,depth+1,execfuncdetail,allfn,middlefunc,ef,detailreport,wfuncsetreturn,copy.copy(pathroad), copy.copy(call_stack), proj=proj)

def reversetrans(nodeset,function,offset,alldata,execfuncdetail,allfuncn,ef,detailreport,wfuncsetreturn, proj):
    node = nodeset[0]
    ti = func2traceinfo(function,node.beginaddr)
    middlefunc = dict()
    reversetracedfs(nodeset,ti,offset,alldata,0,1,execfuncdetail,allfuncn,middlefunc,ef,detailreport,wfuncsetreturn, list(), list(), proj=proj)
    return middlefunc

def writetime(filename,promt,time):
    f = open(filename,"a")
    f.write(promt + "\n")
    f.write(str(time))
    f.write("\n")
    f.close()

def transbin2IR(filename,outputname,importfc = dict()):
    # Important
    result = dict()
    global nextblocktime
    nextblocktime = 0
    detailreport = dict()
    # function detail: function name -> class function
    funcnameset,funcdetail,ruledesdic,wfuncsetreturn,wfuncdetail = rulematch()
    outputtime = outputname + "time"
    # print("time:%s"%outputtime)
    funcnameset = funcnameset.union(list(importfc.keys()))
    funcdetail.update(importfc)
    print("beginlift")
    testbegintime = time.time()
    try:
        # lcom means line comment
        binfile,allfunc,allfuncname,lcom,pltstype,rodatatype,datatype,functiondata,functionsp,innerfunctions,externfunctions,functionmap,alldata,externfuncset = binlcominfo(filename)
    except Exception as e:
        import traceback
        traceback.print_exc(file=sys.stdout)
    if os.path.getsize(binfile) // float(1024*1024) > 10:
        return result,detailreport
    print("size:%d"%os.path.getsize(binfile))
    #if len(externfuncset&funcnameset) == 0:
    #	return result,detailreport
    exportedfunc = nmfile(binfile)
    print("binfile:" + binfile)
    proj = angr.Project(binfile,load_options={'auto_load_libs': False})
    report.extracted_binaries.add((proj.arch.name, binfile))	
 
    # offset = 0 if executable
    # offset = 0x400000 if shared lib
    resulttype,offset = execorlib(binfile)
    cfg = None
 
    # Stage-4: Lifting to IR
    a = time.time()
    try:
        if resulttype == FILETYPE.Vxexec:
            cfg = proj.analyses.CFG()
        else:
            cfg = proj.analyses.CFG()
    except BaseException:
        print("BaseException")
        testendtime = time.time()
        wtime = testendtime-testbegintime
        writetime(outputtime,"lift to IR",wtime)
        print("lift to IR %f"%wtime)
        return result,detailreport
 
    # except Exception:
    # 	testendtime = time.time()
    # 	wtime = testendtime-testbegintime
    # 	writetime(outputtime,"lift to IR",wtime)
    # 	print("lift to IR %f"%wtime)
    # 	print("Exception")
    # 	return result,detailreport
    funcdic = dict(proj.kb.functions)
    msg = ""
    alladdrset = set()
    #wfd = open("/home/zhangli/zhangli/1.txt","w")
    # Meaningless
    # for item in funcdic:
    # 	d = funcdic[item]
    # 	#print(dir(d))
    # 	blockset = d.block_addrs_set
    # 	bl = list(blockset)
    # 	for b in bl:
    # 		block = proj.factory.block(b)
    # 		irsb = block.vex
    # 		functionnode = problock(irsb,lcom)
    # 		#msg = functionnode.getstr()
    # 		#wfd.write(msg)
    #wfd.close()
    # testendtime = time.time()
    # print("endlift")
    # wtime = testendtime-testbegintime
    # writetime(outputtime,"lift to IR",wtime)
    # print("lift to IR %f"%wtime)
    externfunctiondic.clear()
    for item in funcdic:
        alladdrset = alladdrset.union(funcdic[item].block_addrs_set)
    mycfg = dict()
    testbegintime = time.time()
    global starttime
    # Construct cfg
    for item in funcdic:
        if len(funcdic[item].block_addrs_set) == 0:
            continue
        b = funcdic[item].addr
        if b in mycfg:
            continue
        block=proj.factory.block(b)
        irsb = block.vex
        node=problock(irsb,lcom)
        starttime = time.time()
        node, leafset = constructmycfg(node,proj,functionmap,lcom,mycfg,alladdrset,copy.copy(list()),0,None)
        # b is an address of a function
        # leafset means ret or exit statement
        mycfg[b] = [node, leafset]
    testendtime = time.time()
    wtime = testendtime-testbegintime
    writetime(outputtime,"construct cfg",wtime)
    print("construct cfg %f"%wtime)
    print(nextblocktime)
    # parse taint source (target functions)
    execfuncset,execfuncdetail = execfunction()
    for key in lcom:
        if not len(lcom[key]) == 0:
            lcom[key] = lcom[key][1:]
    b_ = time.time()
    report.stage4_time += b_ - a
   
    # Stage-5: Taint analysis
    a = time.time()
    for item in externfunctiondic:
        for elitem in externfunctiondic[item]:
            if not elitem.getexternfun() in funcnameset:
                continue
            function = funcdetail[elitem.getexternfun()]
            print(elitem.getexternfun())
            # elitem.getparents = its callsites
            # Start taint analysis from callsites
            for pitem in elitem.getparents():
                finishfuncdetail(function,pitem[0])
                #global starttime
                starttime = time.time()
                tmpresult = reversetrans(pitem,function,offset,alldata,execfuncdetail,allfuncname,exportedfunc,detailreport,wfuncsetreturn, proj=proj)
                result.update(tmpresult)
    b = time.time()
    report.stage5_time += b - a
 
    return result,detailreport
