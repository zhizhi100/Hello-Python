'''
Created on 2015-5-29

@author: ZhongPing
'''

import wmi
from tornadoweb.pyalbum.picdao import Picdao
def test():

    img = Picdao()
    img.addfile("IMG_20130912_212354.jpg", "E:\weiyun")
    rows = img.queryfile()
    for row in rows:
        print(row)
    
def getlogicdrive():
    c = wmi.WMI()
    

if __name__ == '__main__':
    test()