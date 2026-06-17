from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore_view, name='skills_home'),
    path('explore/', views.explore_view, name='explore'),
    path('add/', views.add_skill, name='add_skill'),
    path(
        'edit/',
        views.edit_skills,
        name='edit_skills'
    ),
    path(
        'recommendations/',
        views.recommendations,
        name='recommendations'
    )
]
