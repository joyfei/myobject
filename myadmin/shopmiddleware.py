# 自定义中间件类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse

import re

class ShopleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print('ShopleMiddleware')

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path =request.path
        print('url:',path)

        #判断登录后台是否登录
        #判断当前请求url地址是否是以/myadmin开头,并且不在urlist
        urllist=['/myadmin/login','/myadmin/logout','/myadmin/dologin','/myadmin/verify']
        if re.match('^/myadmin',path) and (path not in urllist):
            #判断是否登录
            if 'adminuser' not in request.session:
                #重定向到登录页
                return redirect(reverse('myadmin_login'))

        # 判断当前请求是否是访问网站前台
        if re.match(r"^/web", path):
            # 判断当前用户是否没有登录
            if "webuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('web_login'))


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response