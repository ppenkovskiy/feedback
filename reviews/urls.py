from django.urls import path
from .views import review
from django.urls import path, include


urlpatterns = [
    path("", review),
]