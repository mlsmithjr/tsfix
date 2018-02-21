# tsfix
Fix accidentally changed timestamps of a directory of files from an original without recopying

### Set new file "last update" timestamps in a folder from a source copy

A good example of this is your media library when migrating to a new server.  You may want to keep the original timestamps.  But now you've spent hours
copying everything and don't want to do it again just to get those timestamps back.  This script will help.
#
### Requirements.
The source and target folders must be the same structure and mostly the same files.  Any files not found in the target obviously won't be changed.
Only the TIMESTAMP is updated - not the file itself.

Usage:
```
 python3 tsfix /srcdir /targetdir
```

