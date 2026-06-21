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
    path(
        'goal/<int:goal_id>/complete/',
        views.complete_goal,
        name='complete_goal'
    ),

    path(
        'lesson/<int:lesson_id>/complete/',
        views.complete_lesson,
        name='complete_lesson'
    ),
    path(
        "workspace/<int:workspace_id>/generate-flashcards/",
        views.generate_flashcards,
        name="generate_flashcards"
    ),
    path(
        "flashcard/<int:card_id>/delete/",
        views.delete_flashcard,
        name="delete_flashcard"
    ),
    path(
        'workspace/<int:workspace_id>/quiz/',
        views.flashcard_quiz,
        name='flashcard_quiz'
    ),

    path(
        'flashcard/<int:card_id>/answer/',
        views.check_quiz_answer,
        name='check_quiz_answer'
    ),


]
