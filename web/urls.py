# myobject/web/urls.py

from django.urls import path

from web.views import index

urlpatterns = [
   path('', index.index, name="index"),#前台大堂点餐首页

   # 前台管理员路由
   path('login', index.login, name="web_login"),
   path('dologin', index.dologin, name="web_dologin"),
   path('logout', index.logout, name="web_logout"),
   path('verify', index.verify, name="web_verify"), #验证码

]