import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

urls_perfix = "/"

urls_suffix = [
    (r'/', IndexHandler),
    # "/", IndexHandler,
]

print "in-demo-url:",urls_suffix,type(urls_suffix)