from django.urls import path
from librarian import views

urlpatterns = [
    path('', views.RanderLibrarian.as_view(), name='librarian'),
    path('addBookForm/', views.addBookForm.as_view(), name='librarian'),
    path('page/<str:page_name>', views.addBookForm.as_view(), name='page_content_ajax'),
]
