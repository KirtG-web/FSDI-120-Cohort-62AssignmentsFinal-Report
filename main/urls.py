from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('resources/', views.resources, name='resources'),
    path('clothing/', views.clothing, name='clothing'),
    path('food/', views.food, name='food'),
    path('holidays/', views.holidays, name='holidays'),
    path('landmarks/', views.landmarks, name='landmarks'),
    path('contact/', views.contact, name='contact'),
    path('history/', views.history, name='history'),
    path('language/', views.language, name='language'),
    path('culture/', views.culture, name='culture'),
    path('login/', views.login_view, name='login'),
]
