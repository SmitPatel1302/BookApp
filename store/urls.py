from django.urls import path
from store import views

urlpatterns = [
    path('', views.RenderStore.as_view(), name='store'),
]
