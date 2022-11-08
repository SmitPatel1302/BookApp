from django.urls import path
from librarian import views

urlpatterns = [
    path('', views.RanderLibrarian.as_view(), name='librarian'),
]
