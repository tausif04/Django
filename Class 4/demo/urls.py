from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='reports'),
    path('data/', views.data, name='data'),
    path('loop/', views.loop, name='loop'),
]
