from django.shortcuts import render
from django.utils import timezone
from . import models
import random
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def tocomments(request):
    return render(request, 'comments/comments.html')

def getcomments(request):
    email = request.GET.get('email')
    comments = request.GET.get('comments')
    user_name = request.session['user_name']
    time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    print(email)
    print(comments)
    print(user_name)
    print(time)
    dic = {"user":user_name, "email":email, "comments":comments, "time":time}
    newcomments = models.Comments(id=str(random.randint(1000, 9999)), email=email, comments=comments, user=user_name,date=time)
    newcomments.save()

    return JsonResponse(dic)

def showcomments(request):
    commentslist = models.Comments.objects.all()
    commentslist = serializers.serialize('json', commentslist)
    return JsonResponse({"list": commentslist}, safe=False)

