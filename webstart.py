
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# from url import url

from tornado.options import define, options
# from base import BaseHandler

define("port", default=8888, help="run on the given port", type=int)

define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="ddos_system", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="Leeknet@123", help="database password")

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("hello")
# m = __import__("apps.demo.urls")
# print m 
# print m.demo
# print m.demo.urls
# print m.demo.urls.urls_suffix
# urls = m.demo.urls.urls_suffix
# print urls,type(urls)
# for url in urls:
#     print url[0],url[1]


import glob
app_url_list = glob.glob("apps/*/urls.py")

handlers = []

for urls in app_url_list:
    print urls
    print type(urls)
    urls = urls[:-3]
    print urls
    urls = urls.replace('/','.')
    print urls
    apps_meta = __import__(urls)
    demo_meta = getattr(apps_meta,"demo")
    urls_meta = getattr(demo_meta,"urls")
    urls_suffix = getattr(urls_meta,"urls_suffix")
    print urls_suffix,type(urls_suffix)
    # handlers += urls


    # print m
    # print m.demo
    # print m.demo.urls.urls
    # for url 
# url= [
#         (r'/', MainHandler),
# ]

# url = m.demo.urls.urls_suffix
# print url
# for u in url:
#     print type(u)
#     print type(u[0]),type(u[1])

class Application(tornado.web.Application):
    def __init__(self):
        handlers = None
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            cookie_secret = "6dsfd1oETzKXQs45432334322GaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

       
if __name__ == "__main__":
    main()
    # m = __import__("urls")
    # print m.url

    # print m.demo.code
    # print m.urls
    # print urls.url
