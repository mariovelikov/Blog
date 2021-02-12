from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='user profile'),
    path('signin/', views.SignIn.as_view(), name='sign in'),
    path('signout/', views.SignOut.as_view(), name='sign out'),
    path('signup/', views.SignUp.as_view(), name='sign up')
]

from .receivers import *