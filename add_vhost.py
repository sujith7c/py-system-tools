#!/usr/bin/python
#This script crate Virtual Host for Apache2
import os,sys,re
#Document Directory
doc_root = "/var/www/html/"
apache_conf_dir = "/etc/apache2/"
vr_tag_start = False
Parent_end = False
parent_tag = '\<VirtualHost'
field = 'ServerName'

def get_tag_val(parent_tag,field,content):
 if re.match(parent_tag,content):
   if re.match(field,content):
     field_vals = content.split()
     print field_vals
 else:
   print "no tag match"
   return False


def is_parent(content):
 if content != "":
   if re.match('\<',content):
     return True
   else:
     return False
 else:
   return False

def get_child(parent,content):
 tags = re.split('<',content)
 print tags

def split_tags(content):
 if re.search('\<',content):
   pass

def tag_end(content):
 pass

def get_tag_val(tag,content):
  if re.match(tag,content):
    tags = content.split()
    return tags


   
if os.getuid() != 0:
  print("You need to run this script with root privileges, exiting!")
  sys.exit()
else:
 site = raw_input("Enter the Virtual Host name : ").strip()
 '''TODO:check if this site/server name exis
 iterate through each file and read the ServerName value'''

 split_str = re.split(r'-|\*|_|\.',site)
 str_escaped = re.escape(site)
 fl = open('/etc/apache2/sites-available/magento.conf','r')
 lines = fl.readlines()
 for line in lines:
   #print line.strip('\n')
   if is_parent(line):
     for ln in lines:
       #get_child(ln)
       vals = get_tag_val('ServerName',ln.lstrip())
       
       #get_child(parent,ln) 
       #get_tag_val(parent_tag,field,line)


 print vals

 '''TODO: List the current Virtual Hosts'''


 '''TODO
 if not exister create,open file object and create file'''
