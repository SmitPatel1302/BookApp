from django.urls import path
from index import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('AfterSignup/', views.IndexAfterSignup.as_view(), name='index_after_signup'),
    path('AfterLogin/', views.IndexAfterLogin.as_view(), name='index_after_login'),
]
