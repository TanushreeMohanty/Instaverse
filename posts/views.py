from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

@login_required
def feed(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "feed.html", {"posts": posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")  # Redirect to homepage after posting
    else:
        form = PostForm()
    
    return render(request, "create_post.html", {"form": form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')  # Redirect back to feed
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    
    if request.method == 'POST':
        post.delete()
        return redirect('feed')

    return render(request, 'delete_post.html', {'post': post})