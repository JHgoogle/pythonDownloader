import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.shortcuts import render
from . import models
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here
progress_size = 0
def tosearchmusic(request):
    pass
    return render(request, 'music/musicsearch.html')
def getmusic(request):
    # if request.session.get('is_login', None):  # 不允许重复登录
    #     return redirect('/index/')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Referer': 'https://music.163.com/  ',
    }

    musicname = request.GET.get('music_search')
    print(musicname)
# return render(request, 'music/musicsearch.html')
# 搜索歌曲名
    search_url = 'https://music.163.com/#/search/m/?s=' + musicname + '&type=1'  # 搜索链接
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无页面启动chrome
    chrome_options = chrome_options
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)  # 由于反爬机制，通过webdriver获取页面
    try:
        driver.get(search_url)
        iframe = driver.find_element_by_id('g_iframe')  # 跳转进入iframe里面，获取关键内容
        driver.switch_to.frame(iframe)
    except ConnectionError:
        print('搜索错误')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    List = []  # 存储搜索列表
    num = 1  # 显示排序从1开始
    for value in soup.select("div[class='srchsongst'] div[class^='item f-cb h-flag']"):  # 通过CSS选择器获取关键音乐列表
        newsong = models.SongInfo(song_name=value.b.attrs['title'], singer='/'.join([i.string for i in value.select('a[href^="/artist?"]')]))
        newsong.save()
        dic = {'num': 'null', 'song': 'null', 'id': "null", 'singer': 'null', 'song_sheet': 'null', 'url':'null'}  # 存储进入字典
        dic['num'] = num  # 歌曲排序
        dic['song'] = value.b.attrs['title']  # 歌名
        dic['id'] = value.a.attrs['data-res-id']  # 歌曲id
        dic['singer'] = '/'.join([i.string for i in value.select('a[href^="/artist?"]')])  # 歌手
        # dic['song_sheet'] = value.select('a[class^="s-fc3"]')[0].attrs['title']  # 专辑
        dic['url'] = "http://music.163.com/song/media/outer/url?id=" + dic['id'] + ".mp3"
        List.append(dic)
        num += 1
    print(List)
    int = 0
    if int >= 0 and int <= len(List):
        # song_id = List[num]['id']
        for num in range(3):  # 默认下载前三首歌曲
            download_url = "http://music.163.com/song/media/outer/url?id=" + List[num]['id'] + ".mp3"  # 拼接下载地址
            print('第' + str(num + 1) + '首歌曲正在下载中…………')
            response = requests.get(download_url, headers=headers).content
            f = open("./downloadmusic/" + List[num]['song'] + ".mp3", 'wb')  # 二进制写入
            f.write(response)
            f.close()
            print('下载完成.\n\r')
            num += 1
        else:
            print('全部下载完成！')
    return JsonResponse(List, safe=False)
def showmusic(request):
    musiclist = models.SongInfo.objects.all()
    print(musiclist)
    return render(request, 'music/musicshow.html', {'musiclist': musiclist})
def searchmusic(request):
    if request.method == 'POST':
        musicname = request.POST.get('music_name')
        musiclist = models.SongInfo.objects.filter(Q(song_name__contains=musicname) | Q(singer__contains=musicname))
        print(musiclist)
        return render(request, 'music/musicshow.html', {'musiclist':musiclist})
def progress(request):
    global progress_size
    if progress_size < 100:
        progress_size = progress_size + 10
    return JsonResponse({'size':str(progress_size)}, safe=False)