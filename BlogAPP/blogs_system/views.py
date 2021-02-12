from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView
from django.contrib.auth import mixins as auth_mixins

from BlogAPP.blogs_system.forms import CreateBlogForm, CreatePostForm
from BlogAPP.blogs_system.models import Blog, Post


class LandingPage(ListView):
    template_name = 'index.html'
    model = Blog


class BlogDetailsView(DetailView):
    template_name = 'blogs/details.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post_set.all()
        return context


def search_function(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        context = {
            'post': Blog.objects.all().filter(name=search),
        }
        return render(request, 'blogs/posts/search_post.html', context)


class PostListView(ListView):
    template_name = 'blogs/details.html'
    model = Post


class CreateBlogView(auth_mixins.LoginRequiredMixin, CreateView):
    form_class = CreateBlogForm
    model = Blog
    template_name = 'blogs/create.html'

    def get_success_url(self):
        return reverse_lazy('homepage')


class DeleteBlog(auth_mixins.LoginRequiredMixin, DeleteView):
    template_name = 'blogs/delete_blog.html'
    model = Blog

    def get_success_url(self):
        return reverse_lazy('blog details')


class CreatePost(auth_mixins.LoginRequiredMixin, CreateView):
    template_name = 'blogs/posts/create_post.html'
    form_class = CreatePostForm
    model = Post

    def get_success_url(self):
        return reverse_lazy('blog details')


class DeletePost(auth_mixins.LoginRequiredMixin, DeleteView):
    pass
