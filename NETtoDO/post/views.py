from django.shortcuts import render
from .models import Post
# Create your views here.
def home_page(request):
    post = Post.objects.all()
    return render(request,'post/index.html',{'post' : post } )
def Show_day(request,days_id):
    posts = Post.Days_day.filter