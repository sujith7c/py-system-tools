#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
#Get the file/path as argument

def options(cfg):
  try:
    opts,args = getopt.getopt(sys.argv[1:],"hp:d", ["help","path","date"])
  except getopt.GetoptError:
    usage()
  for opt,arg in opts:
    if opt in ("-h","--help"):
      usage()
    elif opt in ("-p","--path"):
      cfg['path'] = arg
    elif opt in ("-d","--days"):
      cfg['days'] = arg


def usage():
  print "deloldfile --help -p=PATH -d= number of days"

if __name__ == "__main__":
  options(sys.argv[1:])



