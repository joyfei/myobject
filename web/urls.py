# myobject/web/urls.py

from django.urls import path,include

from web.views import index,cart


urlpatterns = [
   path('', index.index, name="index"),#前台大堂点餐首页

   # 前台管理员路由
   path('login', index.login, name="web_login"),
   path('dologin', index.dologin, name="web_dologin"),
   path('logout', index.logout, name="web_logout"),
   path('verify', index.verify, name="web_verify"), #验证码

   #为url路由添加前缀
   path('web/',include([
      path('',index.webindex, name='web_index'),#前台大堂点餐首页
      # 购物车信息管理路由配置
      path('cart/add/<str:pid>', cart.add, name="web_cart_add"), #购物车添加
      path('cart/del/<str:pid>', cart.delete, name="web_cart_del"),#购物车删除
      path('cart/clear', cart.clear, name="web_cart_clear"), #购物车清空
      path('cart/change', cart.change, name="web_cart_change"),#购物车更改
   ]))

]