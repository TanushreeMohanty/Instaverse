from django.contrib import admin
from .models import Post, DirectMessage,Report  # ✅ Import DirectMessage model


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'short_caption', 'total_likes', 'created_at', 'updated_at', 'has_media')
    list_filter = ('created_at', 'user')
    search_fields = ('caption', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Post Details', {
            'fields': ('user', 'caption', 'image', 'video')
        }),
        ('Engagement', {
            'fields': ('likes',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def total_likes(self, obj):
        """Returns the total number of likes on the post."""
        return obj.likes.count()
    
    total_likes.short_description = 'Total Likes'

    def has_media(self, obj):
        """Returns an emoji if the post has an image or video."""
        if obj.image or obj.video:
            return "📸🎥"
        return "❌"
    
    has_media.short_description = "Media"

    def short_caption(self, obj):
        """Displays a truncated version of the caption for better readability."""
        return obj.caption[:30] + "..." if len(obj.caption) > 30 else obj.caption
    
    short_caption.short_description = "Caption"


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'short_message', 'post_preview', 'timestamp')
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
            'classes': ('collapse',)
        }),
    )

    def short_message(self, obj):
        """Displays a truncated version of the message for better readability."""
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    
    short_message.short_description = "Message"

    def post_preview(self, obj):
        """Returns a small preview of the post related to the message."""
        if obj.post:
            return f"📌 {obj.post.caption[:20]}..." if len(obj.post.caption) > 20 else obj.post.caption
        return "No Post"
    
    post_preview.short_description = "Post"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'reason', 'reported_at', 'post_excerpt')
    list_filter = ('reason', 'reported_at')
    search_fields = ('user__username', 'post__caption', 'reason')
    ordering = ('-reported_at',)
    readonly_fields = ('user', 'post', 'reason', 'description', 'reported_at')

    def post_excerpt(self, obj):
        """Show a short preview of the post content."""
        return (obj.post.caption[:50] + "...") if obj.post.caption else "(No Caption)"
    
    post_excerpt.short_description = "Post Preview"
