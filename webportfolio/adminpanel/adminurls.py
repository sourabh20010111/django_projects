from django.urls import path
from . import views

# app_name = "adminpanel"

urlpatterns = [
    path('login/', views.login_auth, name='login'),
    path('logout/', views.logout_auth, name='logout'),

    path('', views.dashboard, name='dashboard'),  # after login, redirect here


    
    path('projects/', views.manage_projects, name='manage-projects'),




    path('resume/', views.manage_resume, name='manage-resume'),
    path('about/', views.manage_about, name='manage-about'),
    
    path('profile/', views.manage_profile, name='manage-profile'),
    
    path('contact/', views.manage_contact, name='manage-contact'),
    path('contact/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
