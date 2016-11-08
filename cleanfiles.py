#!/usr/bin/env python
import sys,time,os,getopt,re
import locale,platform,time
from datetime import datetime,date,time

buffer_size = 1024*5
locale.setlocale(locale.LC_ALL,"")
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

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
    #print str(err)
    sys.exit(2)
  for opt,arg in opts:
    if opt in ("-h","--help"):
      usage()
      exit(1)
    elif opt in ("-p","--path"):
      cfg['path'] = arg
    elif opt in ("-d","--days"):
      cfg['numdays'] = arg
    elif opt in ("-n","--name"):
      cfg['exp'] = arg
    elif opt in ("-t", "--test"):
      src ="/root/test/"
      dst = "/tmp/DI/aacces10.txt"
      fls= list_files(src)
      print fls

    else:
      assert False, "Un handled option"
  #check the file/folde exist
  if (len(cfg['path']) !=0 and len(cfg['exp']) !=0):
    #code to check folder and files
    PATH =  cfg['path']
    files = list_files(PATH)
    matches =  match_files(files,cfg['exp'])
    for match in matches: 
      write_console(match,CYAN)
    if len(cfg['numdays']) !=0):
    """find n days old files in windows and linux"""  
      days = cfg['numdays']
      day_diff = days*60*60*24
      
def usage():
  text = """usage: cleanfiles [--help] [-p <path>] [-d <number of days old>] [-n | --name to match]
  -d number days old file in the specified directory / path eg: -d 3 """
  write_console(text,GREEN)

def list_files(path):
  return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]     

def match_files(files,rgx):
  if isinstance(files,list) and any(files):
    #return [fl for fl in files if re.search(pat,fl)]
    pattern = re.compile(rgx)
    return [fl for fl in files if re.search(pattern,fl)]
  else:
    return False

"""move files basicaly  use copy and delete """
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

"""Format the data in table"""



def has_colours(stream):
  if not hasattr(stream, "isatty"):
    return False
  if not stream.isatty():
    return False # auto color only on TTYs
  try:
    import curses
    curses.setupterm()
    return curses.tigetnum("colors") > 2
  except:
    #guess false in case of error
    return False

def write_console(text,colour):
  if has_colours:
    seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
    sys.stdout.write(seq)
    sys.stdout.write('\n')
  else:
    sys.stdout.write(txt)

"""Find n aged files in a system path"""
def find_n_aged_files(filepath,day): 
  """Calculate the date diff"""
  time_obj = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
  today_st_time = time.mktime(time_obj.tuple())
  time_diff = today_st_time - day 
  """Dectect the OS"""
  if platform.system() == "Windows":
    stat = os.path.getctime(filepath)
    if stat.st_mtime < time_diff:
      return filepath
  elif platform.system() == "Linux":
    stat = os.stat()
    if stat.st_mtime < time_diff:
      return filepath
  else:
    write_console("Unsupported Platform !!!",RED)

has_colours = has_colours(sys.stdout)

if __name__ == "__main__":
  main(sys.argv)
  




