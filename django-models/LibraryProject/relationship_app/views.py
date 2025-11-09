from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views import View

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

from .models import Library
from django.views.generic.detail import DetailView
class LibraryDetailView(View):
    def get(self, request, **kwargs):
        library = Library.objects.get(id=kwargs['library_id'])
        return render(request, "relationship_app/library_detail.html", {"library": library})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')  # change to homepage later if needed
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


from django.contrib.auth.decorators import user_passes_test, login_required

# Helper functions to check roles
def admin_check(user):
    return user.userprofile.role == "Admin"

def librarian_check(user):
    return user.userprofile.role == "Librarian"

def member_check(user):
    return user.userprofile.role == "Member"


@login_required
@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@login_required
@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@login_required
@user_passes_test(member_check)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
