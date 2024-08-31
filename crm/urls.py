from django.urls import path, include
from crm import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path("", views.get_home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:record_id>/', views.show_record, name='show_record'),
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),
    path('add_records/', views.add_records, name='add_records'),
    path('update_record/<int:record_id>/', views.update_record, name='update_record')
]