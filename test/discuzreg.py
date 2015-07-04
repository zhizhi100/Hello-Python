# encoding: utf-8
'''
Created on 2015年6月30日

@author: ZhongPing
'''
import urllib
import urllib2
import cookielib
import re
#from cookielib import CookieJar

def demo():
    auth_url = 'http://localhost/upload/admin.php?'
    home_url = 'http://localhost/upload/admin.php?'
    # 登陆用户名和密码
    data={
        "admin_username":"admin",
        "admin_password":"123456",
        'frames':'yes',
        'admin_questionid':'0',
        'submit':'提交'
    }
    # urllib进行编码
    post_data=urllib.urlencode(data)
    # 发送头信息
    headers ={
        "Host":"localhost", 
        "Referer": "http://localhost/upload/admin.php?"
    }
    # 初始化一个CookieJar来处理Cookie
    cookieJar=cookielib.CookieJar()
    # 实例化一个全局opener
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    # 获取cookie
    req=urllib2.Request(auth_url,post_data,headers)
    result = opener.open(req)
    # 访问主页 自动带着cookie信息
    result = opener.open(home_url)
    # 显示结果
    #print result.read()
    #opener.open(url)
    url = 'http://localhost/upload/admin.php?action=members&operation=add'
    req=urllib2.Request(url)
    result = opener.open(req)
    tpage = result.read()
    #print(tpage)
    #print(tpage.find('<input type="hidden" name="formhash" value="'))
    i = tpage.find('<input type="hidden" name="formhash" value="')
    tpage = tpage[i:100+i]
    print(tpage)
    #print('--------------------')
    pattern = re.compile(r'<input type="hidden" name="formhash" value="(\w+)" />')
    match = pattern.match(tpage)
    formhash = '' 
    if match:
        #print(tpage)
        #print(match.groups())
        formhash = match.groups()[0]
    print(formhash)
    # 显示结果
    #print result.read()
    values = {'formhash':formhash,'newusername':'zhp349','newpassword':'123456','newemail':'asdfsdfds349@dsf1d.com','newgroupid':'10','emailnotify':'0','addsubmit':'提交'}
    data = urllib.urlencode(values) 
    req=urllib2.Request(url,data,headers)
    response = opener.open(req)
    the_page = response.read()
    print the_page 

def login():
    url = 'http://localhost/upload/admin.php?'
    values = {'frames':'yes','admin_username':'admin','admin_password':'123456','admin_questionid':'0','addsubmit':'提交'}
    data = urllib.urlencode(values)
    print(data)
    cj=cookielib.CookieJar()   #获取cookiejar实例
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    req = opener.open(url, data)
    content=req.read()
    print(cj)   
    #print(content)    #linux下没有gbk编码，只有utf-8编码
    url = 'http://localhost/upload/admin.php?action=members&operation=add'
    values = {'formhash':'b9437c7e','newusername':'zhp347','newpassword':'123456','newemail':'asdfsdfds347@dsf1d.com','newgroupid':'10','emailnotify':'0','addsubmit':'提交'}
    data = urllib.urlencode(values) 
    req=urllib2.Request(url,data,headers)
    response = opener.open(req)
    the_page = response.read()
    print the_page
    
def reg():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'ZP2b_2132_saltkey=kNfCMVN3; ZP2b_2132_lastvisit=1435659171; ZP2b_2132_auth=40dbsHbBm1%2BdyrZo8cztyldiDGRcD5%2FHMiA3Hl0I%2BnxAuap3OY7UplWXiGMVPLLr7zRhhfo%2FDjlcSb9kJi%2BH; ZP2b_2132_checkpatch=1; ZP2b_2132_checkupgrade=1; ZP2b_2132_ulastactivity=52ed6HWPHp39VDHEjaeMIoI8fp3%2FSIkHaiNoYBphdveI8TNIQEfZ; ZP2b_2132_lip=%3A%3A1%2C1435713695; ZP2b_2132_lastact=1435713699%09admin.php%09; ZP2b_2132_sid=uNx7XX'))
    url = 'http://localhost/upload/admin.php?action=members&operation=add'
    '''
    #values = {'formhash':'49c1d46e','rW4A6S':'zhp3','U020v0':'123456','Rsv055':'123456','VLy9C5':'zhiz13@qq.com'}
    '''
    values = {'formhash':'b9437c7e','newusername':'zhp346','newpassword':'123456','newemail':'asdfsdfds346@dsf1d.com','newgroupid':'10','emailnotify':'0','addsubmit':'提交'}
    data = urllib.urlencode(values)
    print data
    '''req = opener.open(fullurl, data, timeout)(url, data)
    response = urllib2.urlopen(req)'''
    response = opener.open(url, data)
    the_page = response.read()
    print the_page

if __name__ == '__main__':
    #reg()
    #login()
    demo()
    pass