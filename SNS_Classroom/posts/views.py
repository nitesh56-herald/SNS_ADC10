from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from posts.models import *

# Create your views here.
def view_create_post(request):
    return render(request,'createPost.html')

def create_post(request):
    get_author = request.POST['author']
    get_postTitle = request.POST['postTitle']
    get_postContent = request.POST['postContent']
    uploaded_file = request.FILES.get("postFile")
    fs = FileSystemStorage()
    get_postImage =fs.save(uploaded_file.name,uploaded_file)
    postObj = Post(author=get_author,postTitle=get_postTitle,postContent=get_postContent,postFiles=get_postImage)
    postObj.save()
    return redirect('/posts/create')

