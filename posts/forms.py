from django import forms
from .models import Post,DirectMessage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image', 'video']

class DirectMessageForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ['receiver', 'message']