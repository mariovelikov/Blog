from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView
from django.contrib.auth import mixins as auth_mixins, get_user_model
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


# def search_function(request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         context = {
#             'post': Blog.objects.all().filter(name=search),
#         }
#         return render(request, 'blogs/posts/search_post.html', context)


class PostListView(ListView):
    template_name = 'blogs/details.html'
    model = Post


class CreateBlogView(auth_mixins.LoginRequiredMixin, CreateView):
    form_class = CreateBlogForm
    model = Blog
    template_name = 'blogs/create.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        valid = super().form_valid(form)
        todo = form.save()
        todo.user = self.request.user.profile
        todo.save()
        return valid


class DeleteBlog(auth_mixins.LoginRequiredMixin, DeleteView):
    template_name = 'blogs/delete_blog.html'
    model = Blog

    def get_success_url(self):
        return reverse_lazy('homepage')


class CreatePost(auth_mixins.LoginRequiredMixin, CreateView):
    template_name = 'blogs/posts/create_post.html'
    form_class = CreatePostForm
    model = Post
    success_url = '/'

    def form_valid(self, form):
        valid = super().form_valid(form)
        post = form.save()
        post.user = self.request.user.profile
        post.save()
        return valid


class DeletePost(auth_mixins.LoginRequiredMixin, DeleteView):
    template_name = 'blogs/delete_blog.html'
    model = Post

    def get_success_url(self):
        return reverse_lazy('homepage')
