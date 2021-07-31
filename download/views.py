from django.shortcuts import render
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
# Create your views here.
def todownload(request):
    filename = '可乐1.jpg'
    file = open('downloadpic/' + filename, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(filename))
    return response