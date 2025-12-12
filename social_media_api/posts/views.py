from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = '/'

class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detailview.html'
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_createview.html'
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_updateview.html'
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_deleteview.html'
    success_url = '/'