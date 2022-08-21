from django.urls import path
from resume.views import Home

urlpatterns = [
    path('home', Home.as_view() ),
]