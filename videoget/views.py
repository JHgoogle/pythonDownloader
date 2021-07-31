from django.shortcuts import render
import os
import requests
from bs4 import BeautifulSoup
from . import models
import urllib
import time
import subprocess
import json
from django.http import JsonResponse
# Create your views here.
progress_size = 0
def tosearchvideo(request):
    pass
    return render(request, 'video/videosearch.html')

def getvideo(request):

    videoname = request.GET.get('video_search')
    print(videoname)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Referer': 'https://search.bilibili.com/',
    }
    search_url = 'https://search.bilibili.com/all?keyword=' + videoname
    response = requests.get(url=search_url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    sp = soup.prettify()
    # print(soup.prettify())
    List = []
    num = 1
    for value in soup.select(".video-list .video-item"):
        dic = {'id': 'null', 'video': 'null', 'author': 'null', 'playtime': 'null', 'url': 'null'}
        dic['id'] = num
        dic['video'] = value.a.attrs['title']
        video2 = dic['video']
        dic['author'] = '/'.join([i.string for i in value.select('.up-name')])
        dic['playtime'] = soup.find('span', title='观看').text.strip()
        url = value.a.attrs['href']
        dic['url'] = url[2:-12]
        url2 = dic['url']
        cmd_download = "you-get -o ./downloadvideo {}".format(url2)
        os.system(cmd_download)
        print(cmd_download)
        fsize = os.path.getsize('./downloadvideo/' + video2 + '.flv')
        fsize = fsize / float(1024 * 1024)
        size = round(fsize, 2)
        print(size)
        # 未完成
        # r = subprocess.Popen(cmd_getsize, stdout=subprocess.PIPE, shell=True)
        # res = r.stdout.read()
        # res = json.loads(res)
        # video_size = res['streams'].items()
        # print(video_size)
        newvideo = models.VideoInfo(video_name=dic['video'], video_author=dic['author'], video_url=dic['url'], video_size=size)
        newvideo.save()
        List.append(dic)
        if num == 1:
            break
        num += 1
    print(List)
    return JsonResponse(videoname, safe=False)

def showvideo(request):
    videolist = models.VideoInfo.objects.all().distinct()
    print(videolist)
    return render(request, 'video/videoshow.html',{'videolist':videolist})

def searchvideo(request):
    pass
    return render(request, 'video/videoshow.html')

def progress(request):
    global progress_size
    if progress_size < 100:
        progress_size = progress_size + 10
    return JsonResponse({'size':str(progress_size)}, safe=False)