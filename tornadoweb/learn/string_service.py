# encoding: utf-8
'''
Created on 2015年5月27日

@author: ZhongPing
'''
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import os.path

from tornado.options import define, options
from chunk import Chunk

define("port", default=80, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
    def get(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
        
class ImgHandler(tornado.web.RequestHandler): 
    def get(self):
        #self.add_header("Accept-Ranges", "bytes")
        #self.add_header("Connection", "keep-alive")
        #self.add_header("Content-Type", "image/jpg")
        #size = os.path.getsize("E:\\weiyun\\IMG_20130912_212419.jpg")
        #self.add_header("Content-Length", str(size))
        self.set_header('Content-Type', 'image/jpg')

        f = open("E:\\weiyun\\IMG_20130912_212419.jpg","rb")
        try:
            while True:
                chunk = f.read(512*1024)
                if not chunk:
                    break
                self.write(chunk)
        finally:
            f.close()    
        self.finish()
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "debug" : True
    }
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler),
            (r"/img", ImgHandler)
        ],debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()