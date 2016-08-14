#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
#Get the file/path as argument

def main(cfg):
  cfg = {}
  cfg['path']=""
  cfg['numdays']="" 
  try:
    opts,args = getopt.getopt(sys.argv[1:],"?q:h:p:d:e:", ["help","path","date","expression"])
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
    elif opt in ("-e","--regx"):
      cfg['exp'] = arg
    else:
      assert False, "Un handled option"
##------------------Write Logic for file Deletion 
  #check the file/folde exist
  if len(cfg['path']) !=0:
      #code to check folder and files



def usage():
  print "cleanfiles --help -p PATH -d number of days"

if __name__ == "__main__":
  main(sys.argv)
  




