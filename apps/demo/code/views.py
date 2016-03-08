# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web
import json

class UsersHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        users = get_users()
        # self.write(json.dumps(users))
        self.render('show_users.html',users = users)