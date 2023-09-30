import magic
import time
import os
import subprocess

def get_filetype(data,mime=True):
	return magic.from_file(data,mime)

def form_filename(filename):
	result = filename
	result = result.replace("(","\\(")
	result = result.replace(")","\\)")
	return result

def get_dir(filename):
	result = ""
	if not filename.find("/") == -1:
		result = filename[0:filename.rindex("/")]
	else:
		pass
	return result

def get_filename(filename):
    result = ""
    if filename.find("/") == -1:
        result = filename
    else:
        result = filename[filename.rindex("/") + 1:len(filename)]
    return result

def nmfile(sofile):
	result = set()
	sofile = form_filename(sofile)
	filetype = get_filetype(sofile)

	if filetype != b"application/x-sharedlib":
		return result

	output = os.popen("nm -D " + sofile)
	allline = output.read().split("\n")
	for line in allline:
		field = line.split(" ")
		if len(field) != 3 or field[1] != "T":
				continue
		result.add(field[2])
	return result

def challown(filename):
	filename = form_filename(filename)
	os.ystem("chown $USER:$USER " + filename)


def mkdir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def getfileowner(filename):
	filename = form_filename(filename)
	(status,output) = subprocess.getstatusoutput('ls -al ' + filename)
	print(filename)
	print(output)
	result = output.split()[2]
	return result

# def get_filename(fullpath):
#     filename = ""
    
#     if fullpath.find("/") == -1:
#         filename = fullpath
#     else:
#         filename = fullpath[fullpath.rindex("/")+1:len(fullpath)]

#     return filename

def writetime(filename, time, promt):
	f = open(filename,"a")
	f.write(promt + "\n")
	f.write(str(time))
	f.write("\n")
	f.close()

def write_endtime(outputtime, testbegintime, promt):
	testendtime = time.time()
	wtime = testendtime - testbegintime
	writetime(outputtime, wtime, promt)
	print(promt + "\n" + wtime)