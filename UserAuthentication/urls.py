from django.urls import path
from UserAuthentication import views

urlpatterns = [
    path('', views.RenderUserAuthentication.as_view(), name='auth'),
    path('login/', views.RenderLogin.as_view(), name='login'),
    path('signup/', views.RenderSignup.as_view(), name='signup'),
    path('loginDate', views.LoginData.as_view(), name='loginData'),
    path('signupData', views.SignupData.as_view(), name='signupData'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
