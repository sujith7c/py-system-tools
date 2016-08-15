#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
#Get the file/path as argument

def main(cfg):
  cfg = {}
  cfg['path']=""
  cfg['numdays']="" 
  try:
    opts,args = getopt.getopt(sys.argv[1:],"?q:h:p:d:n:", ["quite","help","path","date","name"])
    print opts
  except getopt.GetoptError, err:
    usage()
    print str(err)
    sys.exit(2)
  for opt,arg in opts:
    if opt in ("-h","--help"):
      usage()
      exit(2)
    elif opt in ("-p","--path"):
      cfg['path'] = arg
    elif opt in ("-d","--days"):
      cfg['numdays'] = arg
    elif opt in ("-n","--name"):
      cfg['exp'] = arg
    else:
      assert False, "Un handled option"
##------------------Write Logic for file Deletion 
  #check the file/folde exist
  if len(cfg['path']) !=0:
    #code to check folder and files
    print cfg['path']
    PATH =  cfg['path']

def usage():
  print "cleanfiles --help -p PATH -d number of days"

def list_files(path):
  files = [file for file in os.listdir(PATH) if os.path.isfile(os.path.join(PATH,file))]    

def exclude_files(path):
  pass
  #code to exclude list

def move_files(source,destination):
  #code to move files
  pass

def delete_files(files):
  #code to remove files
  pass

  
if __name__ == "__main__":
  main(sys.argv)
  




