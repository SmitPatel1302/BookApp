from django.urls import path
from UserAuthentication import views

urlpatterns = [
    path('', views.RenderUserAuthentication.as_view(), name='auth'),
    path('login/', views.RenderLogin.as_view(), name='login'),
    path('signup/', views.RenderSignup.as_view(), name='signup'),
]
