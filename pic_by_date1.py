#-------------------------------------------------------------------------------
# Name:module1
# Purpose:
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, os.path
import time
import os, winshell
from win32com.client import Dispatch
import win32api
import re
shell = Dispatch('WScript.Shell')
lnk_re = re.compile(".*lnk$")

def link_from_dir(SOME_DIR = r"C:\\temp\pics_test", LINK_TO_DIR = "", depth = 0):
    if (LINK_TO_DIR == ""):
        LINK_TO_DIR = SOME_DIR
    max_depth = 10
    print "searcging in dir "+ SOME_DIR + " Linking to dir:" + LINK_TO_DIR +" with depth  {0:}".format(depth)
    if (depth > max_depth):
        return(False)
    for filename in os.listdir(SOME_DIR):
        if (lnk_re.match(filename)):
            print filename + " is shrtct, skipping"
            continue
        fullpath = os.path.join(SOME_DIR, filename)
        if os.path.isdir(fullpath):
            dp = depth+1
            link_from_dir(SOME_DIR = fullpath, LINK_TO_DIR = LINK_TO_DIR,depth = dp)
            continue
        mtm = os.path.getmtime(fullpath)
        # strtm = time.strftime('%m/%d/%Y', time.gmtime(mtm))
        lnk_dir_name = time.strftime('pics_%Y_%m', time.gmtime(mtm))
        print filename+" will be linked to  "+lnk_dir_name
        dirpath = os.path.join(LINK_TO_DIR, lnk_dir_name)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        filename_lnk = "{0:}{1:}".format(filename,'.lnk')
        flinkpath = os.path.join(dirpath, filename_lnk)
        if os.path.isfile(flinkpath):
            print "Link Already exists, skipping"
            next
        # Now create the shortcut:
        shortcut = shell.CreateShortCut(flinkpath)
        shortcut.Targetpath = fullpath
        shortcut.WorkingDirectory = SOME_DIR
        # shortcut.IconLocation = icon
        shortcut.save()
    pass

if __name__ == '__main__':
    # link_from_dir()
    link_from_dir(SOME_DIR = r"D:\aaa\restore_debris", LINK_TO_DIR = "D:\pic_links")
