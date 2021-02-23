from django.contrib.auth import get_user_model
from django.db import models
from BlogAPP.authentication.models import Profile

UserModel = get_user_model()


class Blog(models.Model):
    slug = models.SlugField(editable=False)
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='BlogsImage', null=True, blank=False)
    description = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='PostsImage', null=True, blank=False)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
