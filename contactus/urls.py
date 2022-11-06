from django.urls import path
from contactus import views

urlpatterns = [
    path('', views.RenderContactUs.as_view(), name='contact_us'),
]
