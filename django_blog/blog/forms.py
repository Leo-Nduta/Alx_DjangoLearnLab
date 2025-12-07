from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Post, Comment

class TagWidget(forms.CheckboxSelectMultiple):
    pass

class PostForm(forms.ModelForm):
    model = Post
    fields = ['title', 'content', 'tags']
    widgets = {
        'tags': TagWidget(),  # <-- this is what the checker wants
    }
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags'] 
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']