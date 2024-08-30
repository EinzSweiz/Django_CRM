from django.urls import path, include
from crm import views

urlpatterns = [
    path("", views.get_home, name='home'),
]