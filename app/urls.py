from . import views
from .views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('bolg/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path("blogs/<str:username>", views.UserBlogList.as_view(), name='user_blogs'),
    path("blog/create", views.BlogCreateView.as_view(), name='blog_create'),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name='blog_update'),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name='blog_delete'),
]
