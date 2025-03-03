from django.urls import path
from .views import create_story, show_stories, delete_story

urlpatterns = [
    path("upload/", create_story, name="create_story"),
    path("show_stories/", show_stories, name="show_stories"),
    path("delete/<int:story_id>/", delete_story, name="delete_story"),
]
