from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')), # Path to redirect for INDEX app
    path('index/', include('index.urls')), # Path to redirect for INDEX app
    path('UserAuthentication/', include('UserAuthentication.urls')), # Path to redirect for AUTH app
    path('store/', include('store.urls')), # Path to redirect for STORE app
    path('about/', include('about.urls')), # Path to redirect for ABOUT app
    path('contact/', include('contactus.urls')), # Path to redirect for CONTACT US app
]
