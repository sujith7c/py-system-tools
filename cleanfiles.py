#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
#Get the file/path as argument

def options(cfg):
  cfg = []
  try:
    opts,args = getopt.getopt(sys.argv[1:],"?qhpd:", ["help","path","date"])
    print opts
  except getopt.GetoptError, err:
    usage()
    print str(err)
    sys.exit(2)
  for opt,arg in opts:
    if opt in ("-h","--help"):
      usage()
    elif opt in ("-p","--path"):
      cfg.append(arg)
    elif opt in ("-d","--days"):
      cfg.append(arg)
    else:
      assert False, "Un handled option"


def usage():
  print "deloldfile --help -p=PATH -d= number of days"

if __name__ == "__main__":
  options(sys.argv)
  ##print sys.argv[1:]




