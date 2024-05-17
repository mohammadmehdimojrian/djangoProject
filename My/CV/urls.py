from django.urls import path
from .views import profile_list

urlpatterns = [
    path('profiles/', profile_list, name='profile_list'),
]
