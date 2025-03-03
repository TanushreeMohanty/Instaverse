from django.contrib import admin
from .models import Story

@admin.register(Story)  # ✅ Alternative to admin.site.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("user", "image", "created_at")  # ✅ Show these fields in the admin panel
    search_fields = ("user__username",)  # ✅ Search by username
    list_filter = ("created_at",)  # ✅ Filter by creation date
