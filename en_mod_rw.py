#!/usr/bin/python
import os,sys
#Check the OS Version
RELEASE_FILE = "/etc/redhat-release"
if os.path.isfile(RELEASE_FILE):
  f=open(RELEASE_FILE,"r")
  fl_str = f.read()
  rel_version = fl_str.split()
  print rel_version
else:
  raise("Unable to find the OS version")


print sys.version_info
if sys.version_info < (2,7):
  print "This programm works only with the Python 2.7"








