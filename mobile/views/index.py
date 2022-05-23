from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

#移动端首页
def index(request):
    # return HttpResponse('欢迎进入移动会员端首页！')

    return render(request,"mobile/index.html")

def register(request):
    '''加载注册/登录页面'''
    return render(request,"mobile/register.html")

def doregister(request):
    '''执行注册/登录'''
    # 登录成功后跳转到店铺选择页面
    pass

def shop(request):
    ''' 呈现店铺选择页面 '''
    return render(request,"mobile/shop.html")

def selectShop(request):
    ''' 执行店铺选择 '''
    # 选择好店铺后会跳转到移动端首页
    pass

def addOrders(request):
    ''' 加载准备下订单页，由会员确认 '''
    return render(request,"mobile/addOrders.html")