#!/usr/bin/python
import os,sys,re
#Check the OS Version
RELEASE_FILE = "/etc/redhat-release"
RWM_FILE = "/etc/httpd/conf.modules.d/00-base.conf"
if os.path.isfile(RELEASE_FILE):
  f=open(RELEASE_FILE,"r")
  rel_list = f.read().split()
  if rel_list[2] == "release" and tuple(rel_list[3].split(".")) < ('8','5'):
    print("so far good")
else:
  raise("Unable to find the OS version")

#Check Apache installed
#TODO 
#


#Test if the rewrite module file present
if os.path.isfile(RWM_FILE):
 print("re write")


##print sys.version_info
##if sys.version_info < (2,7):
##  print "This programm works only with the Python 2.7"###








