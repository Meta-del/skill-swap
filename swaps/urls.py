from django.urls import path
from . import views

urlpatterns = [

    path(
        'send/<int:skill_id>/',
        views.send_request,
        name='send_request'
    ),

    path(
        'inbox/',
        views.inbox,
        name='inbox'
    ),

    path(
        'accept/<int:request_id>/',
        views.accept_request,
        name='accept_request'
    ),

    path(
        'reject/<int:request_id>/',
        views.reject_request,
        name='reject_request'
    ),
]
