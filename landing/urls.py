app_name = "landing"

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.landing, name='home'),
    path('about-us/', views.about, name='about-us'),
    path('academics/', views.academics, name='academics'),
    path('contact/', views.contact, name='contact'),
    path('featured-alumni/', views.featured, name='featured'),
]