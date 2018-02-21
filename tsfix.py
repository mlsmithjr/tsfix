#
# Set new file "last update" timestamps in a folder from a source copy
#
# This script helps you fix a problem where you copy a large collection of files to another volume/machine and didn't preserve the original timestamps.
# A good example of this is your media library when migrating to a new server.  You may want to keep the original timestamps.  But now you've spent hours
# copying everything and don't want to do it again just to get those timestamps back.  This script will help.
#
# Requirements.
# The source and target folders must be the same structure and mostly the same files.  Any files not found in the target obviously won't be changed.
# Only the TIMESTAMP is updated - not the file itself.
#
# Usage:  python3 tsfix /srcdir /targetdir
#

from os import listdir, stat, utime, walk
import time
import sys
from os.path import isfile, join

src = sys.argv[1]
dest = sys.argv[2]

if not src.startswith('/'):
  print('The source directory path must be absolute and not relative')
  exit(0)
if not dest.startswith('/'):
  print('The target directory path must be absolute and not relative')
  exit(0)

srclen = len(src)

def step_into(base):
    for root, dirs, files in walk(base):
        for f in files:
            if f.startswith('.'): continue
            tofix = dest + join(root[srclen:], f)
            s = stat(join(root,f))
            try:
                utime(tofix, (s.st_mtime, s.st_mtime))
                print(tofix)
            except Exception as ex:
                print(ex)
                pass
        for d in dirs:
            if d.startswith('.'): continue
            s = stat(join(root,d))
            tofix = dest + join(root[srclen:], d)
            try:
                utime(tofix, (s.st_mtime, s.st_mtime))
                print(tofix)
            except Exception as ex:
                print(ex)
                pass
            step_into(join(root, d))

step_into(src)

