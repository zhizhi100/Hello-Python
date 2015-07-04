# encoding: utf-8
'''
Created on 2015年7月1日

@author: ZhongPing
'''
import urllib
import urllib2
import cookielib
import re

class Adder(object):
    '''
    classdocs
    '''
    home_url = ''
    admin_user = ''
    admin_password = ''
    formhash = ''

    def __init__(self, url, admin_user, admin_password):
        '''
        Constructor
        '''
        self.home_url = url + "?"
        self.admin_user = admin_user
        self.admin_password = admin_password
        # 初始化一个CookieJar来处理Cookie
        self.cookieJar=cookielib.CookieJar()
        # 实例化一个全局opener
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
        self.headers ={
            "Host":"localhost", 
            "Referer": url
        }
        
    def login(self):
        '''
         管理员登录系统
        '''
        # 登陆用户名和密码
        data={
            "admin_username":self.admin_user,
            "admin_password":self.admin_password,
            'frames':'yes',
            'admin_questionid':'0',
            'submit':'提交'
        }
        # urllib进行编码
        post_data=urllib.urlencode(data)        
        url = self.home_url
        req=urllib2.Request(url,post_data,self.headers)
        result = self.opener.open(req)
        url = self.home_url+'action=members&operation=add'
        req=urllib2.Request(url)
        result = self.opener.open(req)
        tpage = result.read()
        i = tpage.find('<input type="hidden" name="formhash" value="')
        tpage = tpage[i:100+i]
        pattern = re.compile(r'<input type="hidden" name="formhash" value="(\w+)" />')
        match = pattern.match(tpage)
        formhash = ''
        if match:
            formhash = match.groups()[0]
        self.formhash = formhash
        #print(self.formhash)
        
    def adduser(self,uname,upwd,uemail,ugrpid = '10',emailnotify = '0',addsubmit = '提交'):
        '''
        添加用户
        '''
        url = ""
        url = self.home_url+('action=members&operation=add')
        values = {'formhash':self.formhash,
                  'newusername':uname,
                  'newpassword':upwd,
                  'newemail':uemail,
                  'newgroupid':ugrpid,
                  'emailnotify':emailnotify,
                  'addsubmit':addsubmit
        }
        data = urllib.urlencode(values) 
        req=urllib2.Request(url,data,self.headers)
        response = self.opener.open(req)
        the_page = response.read()
        i = the_page.find('<h3>Discuz! 提示</h3><div class="infobox"><h4 class="infotitle2">用户')
        if (i>0):
            print(("用户"+uname+"添加成功！").decode("utf8"))
        else:
            print(("用户"+uname+"添加失败！").decode("utf8"))
        
    def addusers(self,users):
        '''
        批量添加用户
        users : [{'newusername':newusername,
                  'newpassword':newpassword,
                  'newemail':newemail,
                  'newgroupid':'10',
                  'emailnotify':'0',
                  'addsubmit':'addsubmit'
                  },
                ....]
        '''
        self.login()
        for u in users:
            if (hasattr(u, "newgroupid") and hasattr(u, "emailnotify") and hasattr(u, "addsubmit")) :
                self.adduser(u['newusername'], u['newpassword'], u['newemail'], u['newgroupid'], u['emailnotify'], u['addsubmit'])
            else:
                self.adduser(u['newusername'], u['newpassword'], u['newemail'])
                
def readtxt(file):
    users = []
    fo = open(file)
    lines = fo.readlines()
    for l in lines:
        if len(l)>0 :
             u = l.split(",")
             if len(u) == 6:
                 users.append({'newusername':u[0],
                               'newpassword':u[1],
                               'newemail':u[2],
                               'newgroupid':u[3],
                               'emailnotify':u[4],
                               'addsubmit':u[5]                               
                            })
             if len(u) == 3:
                 users.append({'newusername':u[0],
                               'newpassword':u[1],
                               'newemail':u[2]                            
                            })                 
    return users       
            
                        
def main():
    file = 'user.txt'
    home_url = 'http://localhost/upload/admin.php'
    admin = 'admin'
    pwd = '123456'
    adder = Adder(home_url,admin,pwd)    
    users = readtxt(file)
    adder.addusers(users)

def test():
    home_url = 'http://localhost/upload/admin.php'
    admin = 'admin'
    pwd = '123456'
    adder = Adder(home_url,admin,pwd)
    users = []
    s = ''
    i = 0
    while (i<100):
        s = "".join('%d' %i)
        users.append({'newusername':"zhp105"+s,
                  'newpassword':'123456',
                  'newemail':"new105"+s+("@test.com")
                  })
        i = i + 1
    adder.addusers(users)
        
if __name__ == '__main__':
    main()
    pass        