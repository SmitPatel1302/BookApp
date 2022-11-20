from django.urls import path
from store import views

urlpatterns = [
    path('', views.RenderStore.as_view(), name='store'),
    path('singleProduct/', views.RenderSingleProduct.as_view(), name='singleProduct'),
    path('checkout/', views.RenderCheckout.as_view(), name='checkout'),
]
