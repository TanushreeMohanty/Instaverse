from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # ✅ Import timezone
from datetime import timedelta  # ✅ Import timedelta
from .models import Story
from .forms import StoryForm

# Show active stories (last 24 hours)
@login_required
def show_stories(request):
    stories = Story.objects.filter(created_at__gte=timezone.now() - timedelta(hours=24))
    return render(request, "show_stories.html", {"stories": stories})

# Create a new story (image only)
@login_required
def create_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect("show_stories")
    else:
        form = StoryForm()

    return render(request, "upload_story.html", {"form": form})

# Delete a story
@login_required
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id, user=request.user)
    story.delete()
    return redirect("show_stories")
