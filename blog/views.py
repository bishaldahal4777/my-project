from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, post_id):
    post= get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'posts':post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'blog/create_post.html', {'form': form})
    

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect ('blog/post_detail.html', post_id=post.id)
    else:
        form = PostForm(instance=Post)
    return render(request, 'blog/update_post.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return render(request, 'blog/post_list.html', {'post':post})