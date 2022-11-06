from django.urls import path
from about import views

urlpatterns = [
    path('', views.RenderAbout.as_view(), name='about'),
]
