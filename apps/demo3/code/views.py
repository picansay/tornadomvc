# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web


class UsersHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get():
        users = get_users()
        self.render('show_users.html',users = users)