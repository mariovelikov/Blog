from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from BlogAPP.authentication.models import Profile
from BlogAPP.blogs_system.models import Blog

UserModel = get_user_model()


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
    )


class BlogInline(admin.StackedInline):
    model = Blog


class BlogAdmin(admin.ModelAdmin):
    inlines = (BlogInline,)


admin.site.unregister(UserModel)
admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Profile, BlogAdmin)

