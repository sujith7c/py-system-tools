#!/usr/bin/env python
import sys,time,os,getopt
now = time.time()
buffer_size = 1024*5
#Get the file/path as argument

def main(cfg):
  cfg = {}
  cfg['path']=""
  cfg['numdays']="" 
  try:
    opts,args = getopt.getopt(sys.argv[1:],"?q:h:p:d:n:t", ["quite","help","path","date","name","test"])
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
    elif opt in ("-t", "--test"):
      src ="/root/test/acces10.txt"
      dst = "/tmp/DI/aacces10.txt"
      copyfile(src,dst)

    else:
      assert False, "Un handled option"
  #check the file/folde exist
  if len(cfg['path']) !=0:
    #code to check folder and files
    print cfg['path']
    PATH =  cfg['path']

def usage():
  print """usage: cleanfiles [--help] [-p <path>] [-d <number of days old>] \n 
        [-n | --name to match]"""

def list_files(path):
  files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]    

def match_files(files,rgx):
  if isinstance(files,list) and any(files):
    return [fl for fl in files if re.search(rgx,fl)]
  else:
    return False
"""move files essentially use copy and delete """
def move_files(source,destination):
  assert not os.path.isabs(source)
  while 1:
    copy_buffer =  source.read(buffer_size)
    if not copy_buffer:
      break
    destination.write(copy_buffer)
  pass

def delete_files(files):
  #code to remove files
  pass

def copyfile_obj(fsrc,fdst,length=12*1024):
  while 1:
    buffer =  fsrc.read(length)
    if not buffer:
      break;
    fdst.write(buffer)

def copyfile(src,dst):
  for fn in [src, dst]:
    with open(src, 'rb') as fsrc:
      with open(dst, 'wb') as fdst:
        copyfile_obj(fsrc,fdst)


if __name__ == "__main__":
  main(sys.argv)
  




