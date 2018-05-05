# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from models import *
from hashlib import sha1

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #接受用户输入
    post = request.POST
    uname = post['user_name']
    pwd = post['pwd']
    pwd2 = post['cpwd']
    email = post['email']
    #判断两次密码
    if pwd != pwd2:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(pwd)
    pwd3 = s1.hexdigest()

    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = pwd3
    user.uemail = email
    user.save()
    #注册成功，转到登录页面
    return redirect('/user/login/')

