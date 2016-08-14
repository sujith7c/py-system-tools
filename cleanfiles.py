#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
#Get the file/path as argument

def options(cfg):
  cfg = []
  try:
    opts,args = getopt.getopt(sys.argv[1:],"?q:h:p:d:", ["help","path","date"])
    print opts,args
  except getopt.GetoptError, err:
    usage()
    print str(err)
    sys.exit(2)
  for opt,arg in opts:
    if opt in ("-h","--help"):
      usage()
      exit(2)
    elif opt in ("-p","--path"):
      cfg.append(arg)
    elif opt in ("-d","--days"):
      cfg.append(arg)
    else:
      assert False, "Un handled option"
  print cfg


def usage():
  print "cleanfiles --help -p PATH -d number of days"

if __name__ == "__main__":
  options(sys.argv)
  




