from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_member, name='add_member'),
    path('success/', views.member_success, name='member_success'),
]
