#!/usr/bin/env python
import os
import sys
import fnmatch

MAX_BYTES_READ = 1048576
hexsigns=['203d2027273b20666f722824693d303b202469203c207374726c656e2824']
mdsigns=[]

def get_dir():
	dir=[]
	dir.append(sys.argv[1])
	return dir


def get_files(dir):
	files = []
	for directory in dir:	
		for root, directories, filenames in os.walk(directory):
			for filename in filenames:
				if fnmatch.fnmatch(filename, "*.php"): 
					files.append(os.path.join(root,filename))
	return files

get_files(get_dir())

def dump_hex(filename):
        if os.path.exists(filename):
                try:
                    with open(str(filename), "rb") as bytes:
                        hexdump = bytes.read(MAX_BYTES_READ).encode('hex')
                        return hexdump
                except UnicodeEncodeError:
                        hexdump = ""
                        return hexdump
                except IOError:
                        hexdump = ""
                        return hexdump


def check_hex(signatures,files):
	for f in files:
		if os.path.isfile(f):
			hexdump = dump_hex(f)
			for sign in signatures:
				if sign in hexdump:
					if os.path.exists(f):
						#commandString = "chmod 0 " + " " + (f)
						#os.system(commandString)
						print(f)
						break



check_hex(hexsigns,get_files(get_dir()))
