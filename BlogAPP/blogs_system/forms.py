from django.forms import ModelForm

from BlogAPP.blogs_system.models import Blog, Post
from common import form_mixins


class CreationForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('user',)


class CreateBlogForm(form_mixins.BoostrapMixin, CreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('user',)


class CreatePost(form_mixins.BoostrapMixin, CreatePostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()
