"""pythonDownloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import static
from . import settings
from django.urls import path,re_path
from django.views.static import serve
from django.contrib import admin
from django.urls import path
from login import views as loginviews
from musicget import views as musicviews
from picget import views as picviews
from videoget import views as videoviews
from download import views as downloadviews
from downloadurl import views as downloadurlviews
from upload import views as uploadviews
from comments import views as commentsviews
re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
urlpatterns = [
    # 登录注册
    path('', loginviews.login),
    path('admin/', admin.site.urls),
    path('index/', loginviews.index),
    path('login/', loginviews.login),
    path('register/', loginviews.register),
    path('logout/', loginviews.logout),
    # 下载音乐
    path('musicget/', musicviews.getmusic),
    path('tomusicsearch/', musicviews.tosearchmusic),
    path('musicshow/', musicviews.showmusic),
    path('musicsearch/', musicviews.searchmusic),
    path('getprogress/', musicviews.progress),
    # 下载图片
    path('picget/', picviews.getpic),
    path('topicsearch/', picviews.tosearchpic),
    path('picshow/', picviews.showpic),
    path('picsearch/', picviews.searchpic),
    path('getprogress/', picviews.progress),
    # 下载视频
    path('videoget/', videoviews.getvideo),
    path('tovideosearch/', videoviews.tosearchvideo),
    path('videoshow/', videoviews.showvideo),
    path('videosearch/', videoviews.searchvideo),
    path('getprogress/', videoviews.progress),
    # 服务器下载到本地
    path('download/', downloadviews.todownload),
    # 下载到服务器
    path('todownloadurl/', downloadurlviews.todownload),
    path('downloadurl/', downloadurlviews.getfileinfo),
    path('startdownload/', downloadurlviews.startdownload),
    path('pausedownload/', downloadurlviews.pausedownload),
    path('getprogress/', downloadurlviews.progress),
    # 上传
    path('toupload/', uploadviews.toupload),
    path('checkChunk/', uploadviews.checkChunk, name='checkChunk'),
    path('mergeChunks/', uploadviews.mergeChunks, name='mergeChunks'),
    path('upload/', uploadviews.upload, name='upload'),
    # 评论
    path('tocomments/', commentsviews.tocomments),
    path('getcomments/', commentsviews.getcomments),
    path('showcomments/', commentsviews.showcomments),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
