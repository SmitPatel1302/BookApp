from django.urls import path
from UserAuthentication import views

urlpatterns = [
    path('', views.RenderUserAuthentication.as_view(), name='auth'),
]
