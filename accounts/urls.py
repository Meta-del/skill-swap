from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'notifications/',
        views.notifications,
        name='notifications'
    ),
    path(
        'mentors/',
        views.mentors,
        name='mentors'
    ),
    path(
        'profile/<int:user_id>/',
        views.public_profile,
        name='public_profile'
    ),
]
