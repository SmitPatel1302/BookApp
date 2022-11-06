from django.urls import path
from index import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
