from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_members, name='all_members'),
    path('members/', views.members, name='members'),
    path('details/<int:id>', views.details, name='details')
]
