from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})

def post_detail(request):
    pass

def create_post(request):
    pass