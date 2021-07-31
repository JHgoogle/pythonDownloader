from django.shortcuts import render
import urllib
from bs4 import BeautifulSoup
import re
import time
import os
import sys
import hashlib
from . import models
from django.shortcuts import redirect
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
progress_size = 0
def tosearchpic(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    pass
    return render(request, 'picture/picsearch.html')


def getpic(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    user = request.session.get('user_name')
    print(user)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Referer': 'https://music.163.com/  ',
    }
    url = "https://cn.bing.com/images/async?q={0}&first={1}&count={2}&scenario=ImageBasicHover&datsrc=N_I&layout=ColumnBased&mmasync=1&dgState=c*9_y*2226s2180s2072s2043s2292s2295s2079s2203s2094_i*71_w*198&IG=0D6AD6CBAF43430EA716510A4754C951&SFX={3}&iid=images.5599"

    first = 1
    load = 35
    sfx = 1
    count = 0
    total = 3
    rule = re.compile(r'\"murl\"\:"http\S[^\"]+')
    picname = request.GET.get('pic_search')
    word = urllib.parse.quote(picname)
    page = urllib.request.Request(url.format(word, first, load, sfx), headers=headers)
    html = urllib.request.urlopen(page)
    soup = BeautifulSoup(html, 'html.parser')
    pic_list = soup.find_all('a', class_='iusc')
    path = './user/' + user + '/downloadpic/'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        print('文件夹已存在')
    List = []
    for pointer in pic_list:
        result = re.search(rule, str(pointer))
        url = result.group()
        url = url[8:len(url)]
        try:
            time.sleep(0.5)
            urllib.request.urlretrieve(url, path + picname + str(count + 1) + '.jpg')
            dic = {"picname":"null", "url":"null"}
            dic["picname"] = picname + str(count + 1) + '.jpg'
            dic["url"] = url
            List.append(dic)
            fsize =os.path.getsize(path + picname + str(count + 1) + '.jpg')
            fsize = fsize / float(1024 * 1024)
            size = round(fsize, 2)
            print(size)
            with open(path + picname + str(count + 1) + '.jpg', 'rb') as fp:
                data = fp.read()
            md5 = hashlib.md5(data).hexdigest()
            print(md5)
            newpic = models.PicInfo(pic_name=picname + str(count + 1), pic_size=size, pic_md5=md5, user=user,
                                    pic_address=url)
            newpic.save()
            print('下载成功，成功保存' + str(count + 1) + '张图')
            count += 1
            first = count + 1
            sfx += 1
            if count == 3:
                return JsonResponse(List, safe=False)
        except Exception:
            time.sleep(1)
            print('图片出现错误，跳过下载')





def showpic(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    user = request.session.get('user_name')
    piclist = models.PicInfo.objects.filter(user=user)
    print(piclist)
    return render(request, 'picture/picshow.html', {"piclist":piclist})

def searchpic(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    user = request.session.get('user_name')
    if request.method == 'POST':
        picname = request.POST.get('pic_name')
        print(picname)
        piclist = models.PicInfo.objects.filter(user=user).filter(pic_name__contains=picname)
        print(piclist)
    return render(request, 'picture/picshow.html', {"piclist":piclist})

def progress(request):
    global progress_size
    if progress_size < 100:
        progress_size = progress_size + 10
    return JsonResponse({'size':str(progress_size)}, safe=False)