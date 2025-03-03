from django.urls import path
from . import views
from .views import feed, create_post, edit_post, delete_post,like_unlike_post,send_message,inbox,bookmark_post,saved_posts

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', feed, name='feed'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),  # ✅ Correct URL pattern
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('like/<int:post_id>/', like_unlike_post, name='like_post'),
    path('send_message/<int:post_id>/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('bookmark/<int:post_id>/', bookmark_post, name='bookmark_post'),
    path('saved/', saved_posts, name='saved_posts'),

]
