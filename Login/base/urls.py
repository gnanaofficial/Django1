from django.urls import path, include
from .views import authView
urlpatterns = [
   
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
    