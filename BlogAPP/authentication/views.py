from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from BlogAPP.authentication.forms import *
from BlogAPP.blogs_system.models import *


class UserProfile(views.UpdateView):
    template_name = 'authentication/profile.html'
    form_class = UserProfileForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy('homepage')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object().user
        context['current_profile'] = self.get_object().user != self.request.user
        context['blog'] = self.get_object().blog_set.all()
        return context


class SignUp(views.CreateView):
    template_name = 'authentication/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignIn(auth_views.LoginView):
    template_name = 'authentication/signin.html'
    form_class = SignInForm


class SignOut(auth_views.LogoutView):
    next_page = reverse_lazy('homepage')
