from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import Post
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            user = form.save()          # Save the new user to the database
            login(request, user)        # Log in the user immediately
            return redirect('profile')  # Redirect to profile page
    else:
        form = CustomUserCreationForm()  # Empty form for GET request

    return render(request, 'register.html', {'form': form}) 

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)  # Update email
        # Additional fields can be updated here if extended
        user.save()
        return render(request, 'profile.html', {'message': 'Profile updated successfully!'})
    
        if request.FILES.get('profile_pic'):
                profile.profile_pic = request.FILES['profile_pic']

        user.save()
        profile.save()
        return render(request, 'blog/profile.html', {'message': 'Profile updated successfully!'})

#return render(request, 'profile.html'), {'profile' : profile}

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        instance.profile.save()

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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user      # automatically set logged-in user
            post.save()
            return redirect('post_list')     # change name if needed
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user   # ensure correct author
            updated_post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'update_post.html', {'form': form})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post, Comment

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']   # author is set automatically

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, ListView, DetailView

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']   # author is set automatically

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'content']
class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    ordering = ['-date_posted']

class CommentDetailView(DetailView):
    model = Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']   # author is set automatically

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  
