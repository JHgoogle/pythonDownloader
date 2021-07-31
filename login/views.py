from django.shortcuts import render
from django.shortcuts import redirect
from . import models
import random
import os
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        message = '请检查填写的内容！'
        if username.strip() and password:  # 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.UserInfo.objects.get(user_name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})
            if user.user_password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.user_name
                save_path = './user/' + user.user_name
                isExists = os.path.exists(save_path)
                if not isExists:
                    os.makedirs(save_path)
                    print('创建用户' + user.user_name)
                else:
                    print('用户已存在')
                request.session.set_expiry(0)
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username, password1)
        message = '请检查填写的内容！'
        if username.strip() and password1:  # 检查用户名密码是否为空
            if password1 != password2:  # 检查确认密码和密码是否相同
                message = '两次输入密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(user_name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                newuser = models.UserInfo(user_id=str(random.randint(1000, 9999)), user_name=username, user_password=password1)
                newuser.save()
                return redirect('/login/')
        else:
            return render(request, 'login/register.html')
    else:
        return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")