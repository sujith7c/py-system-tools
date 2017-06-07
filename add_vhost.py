#!/usr/bin/python
#This script crate Virtual Host for Apache2
import os,sys,re
#Document Directory
doc_root = "/var/www/html/"
apache_conf_dir = "/etc/apache2/sites-available/"
vr_tag_start = False
Parent_end = False
parent_tag = '\<VirtualHost'
field = 'ServerName'

def get_tag_val(tag,content):
 tags = content.split() if re.match(tag,content) else None 
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
 conf_files = [f for f in os.listdir(apache_conf_dir) if f.endswith('.conf')]
 vhost = []
 #print conf_files
 for cfile in conf_files:
   fl = open(apache_conf_dir+cfile,'r')
   lines = fl.readlines()
   vals = filter(None,[get_tag_val('ServerName',line.lstrip()) for line in lines])
   if len(vals) > 0 :
     vhost.append(vals)
   fl.close()
 print vhost
 '''TODO: List the current Virtual Hosts'''
 '''TODO
 if not exister create,open file object and create file'''
