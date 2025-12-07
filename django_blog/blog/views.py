from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import Post

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

    return render(request, 'profile.html'), {'profile' : profile}
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        instance.profile.save()


