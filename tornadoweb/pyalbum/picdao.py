'''
Created on 2015-5-29

@author: ZhongPing
'''
import sqlite3
import os
import os.path
import hashlib

class Picdao(object):
    '''
    add picinfo into database
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print "inited"
        self.sha1obj = hashlib.sha1()
        self.cx = sqlite3.connect("pyalbum.db")
        self.c = self.cx.cursor()
        self.c.execute("create table if not exists pics (filename text, parent text, hash text,  size UNSIGNED BIG INT, picdate DATETIME)" )
        
    def __del__(self):
        '''
        destroy
        '''
        self.cx.close()
    
    def add(self,fname,fparent,hash,size,picdate):
        '''
        add pic
        '''
        self.c.execute("SELECT count(1) FROM pics WHERE hash=? and size=?",(hash,size))
        r = self.c.fetchone()
        if (r[0] == 0):
            self.c.execute("insert into pics values(?,?,?,?,?)",(fname,fparent,hash,size,picdate))
            #self.c.commit()
     
    def addfile(self,fname,fparent):
        '''
        add pic from file
        '''
        fullname = os.path.join(fparent,fname)
        if (os.path.exists(fullname)):
            with open(os.path.join(fparent,fname),'rb') as f:               
                self.sha1obj.update(f.read())
                hash = self.sha1obj.hexdigest()
            size = os.path.getsize(fullname)
            picdate = os.path.getmtime(fullname)
            self.add(fname, fparent, hash, size, picdate)
                
    def queryfile(self):
        '''
        query files from database
        '''   
        return self.c.execute("select * from pics")