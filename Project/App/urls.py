from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
]

