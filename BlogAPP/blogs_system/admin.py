from django.contrib import admin
from BlogAPP.blogs_system.models import Post, Comment, Blog


class PostInline(admin.StackedInline):
    model = Post


# class CommentInline(admin.StackedInline):
#     model = Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    inlines = (PostInline,)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'user')
    # inlines = (CommentInline,)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
