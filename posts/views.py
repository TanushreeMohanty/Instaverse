from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,DirectMessage,Bookmark
from .forms import PostForm,DirectMessageForm
from django.http import JsonResponse

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

@login_required
def like_unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)  # Unlike
        liked = False
    else:
        post.likes.add(request.user)  # Like
        liked = True

    return JsonResponse({"liked": liked, "total_likes": post.total_likes()})

@login_required
def send_message(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = DirectMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.post = post
            message.save()
            return redirect('inbox')  # Redirect to inbox after sending message

    else:
        form = DirectMessageForm()

    return render(request, 'send_message.html', {'form': form, 'post': post})

@login_required
def inbox(request):
    messages = DirectMessage.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def bookmark_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)

    if created:
        saved = True  # If a new bookmark was created, mark as saved
    else:
        bookmark.delete()  # If already saved, remove it (toggle feature)
        saved = False  # Mark as unsaved

    # Handle both AJAX & normal requests
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"saved": saved})

    return redirect(request.META.get("HTTP_REFERER", "feed"))  # Redirect back to the previous page or feed
@login_required
def saved_posts(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('post')
    return render(request, 'saved_posts.html', {'bookmarks': bookmarks})
