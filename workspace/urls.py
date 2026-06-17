from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:workspace_id>/',
        views.workspace_detail,
        name='workspace_detail'
    ),
    path(
        '<int:workspace_id>/goal/add/',
        views.add_goal,
        name='add_goal'
    ),
    path(
        '<int:workspace_id>/lesson/add/',
        views.add_lesson,
        name='add_lesson'
    ),

    path(
        '<int:workspace_id>/material/add/',
        views.add_material,
        name='add_material'
    ),
    path(
        '<int:workspace_id>/review/',
        views.add_review,
        name='add_review'
    ),
    path(
        'goal/<int:goal_id>/toggle/',
        views.toggle_goal,
        name='toggle_goal'
    ),
    path(
        '<int:workspace_id>/flashcard/add/',
        views.add_flashcard,
        name='add_flashcard'
    ),
    path(
        '<int:workspace_id>/study/',
        views.study_flashcards,
        name='study_flashcards'
    ),
]
