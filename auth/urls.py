from django.urls import path
from auth import views

urlpatterns = [
    path('', views.RenderAuth.as_view(), name='auth'),
]
