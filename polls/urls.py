from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]