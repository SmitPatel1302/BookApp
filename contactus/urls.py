from django.urls import path
from contactus import views

urlpatterns = [
    path('', views.RenderContactUs.as_view(), name='contact_us'),
    path('submitContactForm', views.SubmitContactForm.as_view(), name='submit_contact_form'),
]
