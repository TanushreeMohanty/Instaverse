from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ["image"]

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.content_type.split("/")[0] != "image":
                raise forms.ValidationError("Only image files are allowed!")
        return image
