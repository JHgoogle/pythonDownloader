from django.shortcuts import render
import urllib
import time
import requests
import sys
import os
from django.http import JsonResponse
from urllib.request import urlopen
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
from . import models
import random
import subprocess
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Create your views here.
progress_size = 0
flag = True
speed = 0
def todownload(request):
    pass
    return render(request, 'downloadurl/downloadurl.html')

def getfileinfo(request):
    global num_progress
    downloadurl = request.GET.get('i1')
    print(downloadurl)
    user = request.session.get('user_name')
    path = './user/' + user + '/download_offline/'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        print('文件夹已存在')
    # 第一次请求是为了得到文件总大小
    r1 = requests.get(downloadurl, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])
    total = total_size / (1024 * 1024)
    total = round(total,2)
    name = os.path.basename(downloadurl)
    id = str(random.randint(1000,9999))
    newfile = models.DownloadInfo(id=id, download_url=downloadurl, download_name=name, download_size=total)
    newfile.save()
    rsp = requests.get(downloadurl, stream=True)
    hostip = rsp.raw._connection.sock.getpeername()[0]
    print(hostip)
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        userip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        userip = request.META.get("REMOTE_ADDR")
    print("userip : ", userip)
    dic = {'id': id, 'downloadurl':downloadurl, 'downloadname':name, 'downloadsize':total, 'hostip':hostip, 'userip':userip}
    return JsonResponse(dic)

def startdownload(request):
    global progress_size
    global speed
    global flag
    downloadurl = request.GET.get('url')
    print(downloadurl)
    start_time = time.time()
    user = request.session.get('user_name')
    path = './user/' + user + '/download_offline/'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        print('文件夹已存在')
    # 第一次请求是为了得到文件总大小
    r1 = requests.get(downloadurl, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])
    total = total_size / (1024 * 1024)
    total = round(total, 2)
    name = os.path.basename(downloadurl)
    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(path + name):
        temp_size = os.path.getsize(path + name)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少
    print(temp_size)
    print(str(total) + 'MB')
    # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
    headers = {'Range': 'bytes=%d-' % temp_size}
    # 重新请求网址，加入新的请求头的
    r = requests.get(downloadurl, stream=True, verify=False, headers=headers)
    # 下面写入文件也要注意，看到"ab"了吗？
    # "ab"表示追加形式写入文件
    with open(path + name, "ab") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:

                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                speed = (temp_size /(time.time()-start_time)) / (1024*1024)
                print(speed)
                done = int(50 * temp_size / total_size)
                progress_size = (100 * temp_size / total_size)
                progress_size = round(progress_size,2)
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()

    return JsonResponse(downloadurl,safe=False)

def progress(request):
    global progress
    global speed
    return JsonResponse({'size':str(progress_size), 'speed':str(speed)}, safe=False)

def pausedownload(request):
    global flag
    subprocess.call("pause", shell = True)
    return JsonResponse(flag, safe=False)