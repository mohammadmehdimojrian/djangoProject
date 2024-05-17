from django.shortcuts import render
from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'CV/profile_list.html', {'profiles': profiles})
