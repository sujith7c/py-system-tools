#!/usr/bin/python
#This script crate Virtual Host for Apache2
import os,sys,re
import readline

#Apache Document Directory
doc_root = "/var/www/html/"
apache_conf_dir = "/etc/apache2/sites-available/"
parent_tag = '\<VirtualHost'
field = 'ServerName'
#GNU Auto complete feature
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

def get_tag_val(tag,content):
 if re.match(tag,content.lstrip()):
   meta = content.split()
   tags = {meta[0]:meta[1]}
 else:
   tags = None
   #tags = content.split() if re.match(tag,content.lstrip()) else None
 return tags

def get_vhosts(meta_vhosts):
  vhost_arr = []
  for meta in meta_vhosts:
    for host in meta:
      vhost_arr.append(host['ServerName'])

  return vhost_arr
#check virtual host exist or not
def vhosts_exist(site,metaobjs):
  for obj in metaobjs:
    if obj == site: 
      return True
  return False
#Create the virtual host file in the direcotry
def create_vhost_conf(directory,name):
  try:
    if os.path.isdir(directory):
      try:
        vconfFile = apache_conf_dir + '/' + name + '.conf'
        confile = open(vconfFile,'w')
        fstream =''
        fstream += '<VirtualHost *:80>' + '\n'
        fstream += '  ServerName '+name + '\n'
        fstream += '  DocumentRoot ' + directory + '\n'
        fstream += '  <Directory ' + directory + '/>' + '\n'
        fstream += '    Options Indexes FollowSymLinks MultiViews' + '\n'
        fstream += '    AllowOverride All' + '\n'
        fstream += '  </Directory>' + '\n'
        fstream += '</VirtualHost>' + '\n'
        ret = confile.write(fstream)
        confile.close()
        print ret
      except IOError:
        print "Unable to opne the file for conf file creation"
  except IOError:
    print "Unable to open the target path"

def create_doc_root(directory):
  if os.path.isdir(directory):
    print "Document Root already exist"
  else:
    try:
      os.mkdir(directory)
    except IOError:
      print "Can not make Document root directoy"


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
 vhosts_met = []
 #print conf_files
 for cfile in conf_files:
   fl = open(apache_conf_dir+cfile,'r')
   lines = fl.readlines()
   vals = filter(None,(get_tag_val('ServerName',line) for line in lines))
   if len(vals) > 0 :
     vhosts_met.append(vals)
   fl.close()
 
 '''TODO: List the current Virtual Hosts'''
 vhobj = get_vhosts(vhosts_met)

 '''if not exister create,open file object and create file'''
 ret = vhosts_exist(site,vhobj)
 if ret == True: 
   print('\x1b[6;30;30;30;31m' + 'Vhost Exist! please change the vhost name' + '\x1b[0m')
 else:
   #print('\x1b[6;30;42m' + 'Vhost can be added'  + '\x1b[0m')
   docdir = raw_input("Enter the document directory: ")
   if docdir !="" : 
     create_doc_root(docdir)
     if os.path.isdir(docdir):
       create_vhost_conf(docdir,site)
       print('\x1b[6;30;42m' + 'New Vhost '+ site  +' added'  + '\x1b[0m')     
     else:
       sys.exit("Sys Error!!,contact support")
      

