from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
from .forms import *


class BlogListView(ListView):
    model = Blog
    template_name = 'app/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 6


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app/blog.html'


class UserBlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'app/home.html'
    context_object_name = 'blogs'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user).order_by('-date_posted')


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'app/post.html'
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'app/post.html'
    form_class = BlogForm
    success_message = "Post Updated Successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'app/delete.html'
    success_message = 'Success: Post is successfully deleted'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'app/about.html')
