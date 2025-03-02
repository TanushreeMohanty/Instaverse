from django.contrib import admin
from .models import Post, DirectMessage  # ✅ Import DirectMessage model

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'caption', 'total_likes', 'created_at', 'updated_at', 'image', 'video')
    list_filter = ('created_at', 'user')
    search_fields = ('caption', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Post Details', {
            'fields': ('user', 'caption', 'image', 'video')
        }),
        ('Likes', {
            'fields': ('likes',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def total_likes(self, obj):
        return obj.likes.count()

    total_likes.short_description = 'Total Likes'


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'post', 'message', 'timestamp')
    list_filter = ('timestamp', 'sender', 'receiver')
    search_fields = ('sender__username', 'receiver__username', 'message')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

    fieldsets = (
        ('Message Details', {
            'fields': ('sender', 'receiver', 'message', 'post')
        }),
        ('Timestamps', {
            'fields': ('timestamp',),
        }),
    )
