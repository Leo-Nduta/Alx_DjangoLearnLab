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
    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)

    def render(self, name, value, attrs=None, renderer=None):
        return super().render(name, value, attrs, renderer)

class PostForm(forms.ModelForm):
    new_tags = forms.CharField(
        required=False,
        help_text="Enter new tags separated by commas",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Django, Python'})
    )
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