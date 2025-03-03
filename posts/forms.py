from django import forms
from .models import Post,DirectMessage,Report

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image', 'video']

class DirectMessageForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ['receiver', 'message']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason', 'description']
        widgets = {
            'reason': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
