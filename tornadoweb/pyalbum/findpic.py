'''
Created on 2015-5-28

@author: ZhongPing
'''

import ctypes
import os
import os.path
import time
import hashlib
import sqlite3

lpBuffer = ctypes.create_string_buffer(78)
ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
vol = lpBuffer.raw.split('\x00')
count = 0
t1 = time.time()
cx = sqlite3.connect("pyalbum.db")
for l in vol:
    if l:
        print(l)
        rootdir = l
        for parent,dirnames,filenames in os.walk(rootdir):   
             '''
             for dirname in  dirnames:                       
                 print  "dirname is" + dirname
            '''
             for filename in filenames:
                 '''
                 print "parent is:" + parent
                 print "filename is:" + filename
                 print "the full name of the file is:" + os.path.join(parent,filename) 
                 '''
                 a,b = os.path.splitext(filename)
                 b = b.lower()
                 #print b
                 if (b == ".jpg"):
                    count = count + 1
                    with open(os.path.join(parent,filename),'rb') as f:
                        sha1obj = hashlib.sha1()
                        sha1obj.update(f.read())
                        hash = sha1obj.hexdigest()
                        #print(hash)
t2 = time.time()
print (t2 - t1)
print (count)