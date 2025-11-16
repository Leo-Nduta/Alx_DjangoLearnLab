from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile

@permission_required('relationship_app.can_view', raise_exception=True)
def view_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'relationship_app/profile_detail.html', {'profile': profile})

@permission_required('relationship_app.can_create', raise_exception=True)
def create_profile(request):
    if request.method == "POST":
        # process form submission
        ...
    return render(request, 'relationship_app/profile_form.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        # process form submission
        ...
    return render(request, 'relationship_app/profile_form.html', {'profile': profile})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    profile.delete()
    return redirect('profile_list')