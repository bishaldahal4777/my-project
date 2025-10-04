from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# List all posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list,5)
    page_number = request.Get.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create a new post
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# Update an existing post
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})

# Delete a post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})
