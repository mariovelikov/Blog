from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_blog/', views.CreateBlogView.as_view(), name='create blog'),
    path('<int:pk>/', views.BlogDetailsView.as_view(), name='blog details'),
    path('<int:pk>/delete/', views.DeleteBlog.as_view(), name='delete blog'),

    path('create_post/', views.CreatePost.as_view(), name='create post'),
    # path('<int:pk>/delete_post/', views.DeletePost.as_view(), name='delete post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
