
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Workspace, Lesson, Goal, Material, Message, Review, Flashcard
from .forms import MessageForm
from .forms import GoalForm
from .forms import LessonForm
from .forms import MaterialForm
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Flashcard
from .forms import FlashcardForm
from .models import Progress
from .forms import FlashcardGeneratorForm
from .services import generate_flashcards_from_notes
from .models import Flashcard
from random import choice


def workspace_detail(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )
    flashcards = Flashcard.objects.filter(
        workspace=workspace
    )
    review_form = ReviewForm()

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save(commit=False)

            message.workspace = workspace

            message.sender = request.user

            message.save()

    else:

        form = MessageForm()

    lessons = Lesson.objects.filter(
        workspace=workspace
    )

    goals = Goal.objects.filter(
        workspace=workspace
    )
    total_goals = goals.count()

    completed_goals = goals.filter(
        completed=True
    ).count()

    if total_goals > 0:
        progress = int(
            (completed_goals / total_goals) * 100
        )
    else:
        progress = 0

    materials = Material.objects.filter(
        workspace=workspace
    )

    messages = Message.objects.filter(
        workspace=workspace
    ).order_by('sent_at')
    reviews = Review.objects.filter(
        workspace=workspace
    )
    progress, created = Progress.objects.get_or_create(
        workspace=workspace
    )

    return render(
        request,
        'workspace/detail.html',
        {
            'workspace': workspace,
            'lessons': lessons,
            'goals': goals,
            'materials': materials,
            'messages': messages,
            'form': form,
            'reviews': reviews,
            'progress': progress,
            'review_form': review_form,
            'flashcards': flashcards,


        }
    )


def add_goal(request, workspace_id):

    workspace = Workspace.objects.get(
        id=workspace_id
    )

    if request.method == 'POST':

        form = GoalForm(request.POST)

        if form.is_valid():

            goal = form.save(commit=False)

            goal.workspace = workspace

            goal.save()

    return redirect(
        'workspace_detail',
        workspace_id=workspace.id
    )


def add_lesson(request, workspace_id):

    workspace = Workspace.objects.get(
        id=workspace_id
    )

    if request.method == 'POST':

        form = LessonForm(request.POST)

        if form.is_valid():

            lesson = form.save(commit=False)

            lesson.workspace = workspace

            lesson.save()

    return redirect(
        'workspace_detail',
        workspace_id=workspace.id
    )


def add_material(request, workspace_id):

    workspace = Workspace.objects.get(
        id=workspace_id
    )

    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            material = form.save(
                commit=False
            )

            material.workspace = workspace

            material.save()

    return redirect(
        'workspace_detail',
        workspace_id=workspace.id
    )


@login_required
def toggle_goal(request, goal_id):

    goal = get_object_or_404(
        Goal,
        id=goal_id
    )

    goal.completed = not goal.completed
    goal.save()

    return redirect(
        'workspace_detail',
        workspace_id=goal.workspace.id
    )


@login_required
def add_review(
    request,
    workspace_id
):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    if request.method == 'POST':

        form = ReviewForm(
            request.POST
        )

        if form.is_valid():

            review = form.save(
                commit=False
            )

            review.workspace = workspace
            review.reviewer = request.user

            review.save()

    return redirect(
        'workspace_detail',
        workspace_id=workspace.id
    )


@login_required
def add_flashcard(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    if request.method == 'POST':

        form = FlashcardForm(
            request.POST
        )

        if form.is_valid():

            card = form.save(commit=False)
            card.workspace = workspace
            card.save()

            return redirect(
                'workspace_detail',
                workspace_id=workspace.id
            )

    else:

        form = FlashcardForm()
    return render(
        request,
        'workspace/add_flashcard.html',
        {
            'form': form
        }
    )


@login_required
def study_flashcards(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    flashcards = Flashcard.objects.filter(
        workspace=workspace
    )
    return render(
        request,
        'workspace/study_flashcards.html',
        {
            'workspace': workspace,
            'flashcards': flashcards
        }
    )


@login_required
def complete_goal(request, goal_id):

    goal = get_object_or_404(
        Goal,
        id=goal_id
    )

    goal.completed = True
    goal.save()

    progress, created = Progress.objects.get_or_create(
        workspace=goal.workspace
    )

    progress.goals_completed += 1
    progress.total_points += 5
    progress.save()

    return redirect(
        'workspace_detail',
        workspace_id=goal.workspace.id
    )


@login_required
def complete_lesson(request, lesson_id):

    lesson = get_object_or_404(
        Lesson,
        id=lesson_id
    )

    lesson.completed = True
    lesson.save()

    progress, created = Progress.objects.get_or_create(
        workspace=lesson.workspace
    )

    progress.lessons_completed += 1
    progress.total_points += 10
    progress.save()

    return redirect(
        'workspace_detail',
        workspace_id=lesson.workspace.id
    )


@login_required
def generate_flashcards(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    if request.method == "POST":

        form = FlashcardGeneratorForm(
            request.POST
        )

        if form.is_valid():

            notes = form.cleaned_data["notes"]

            cards = generate_flashcards_from_notes(
                notes
            )

            for card in cards:

                Flashcard.objects.create(
                    workspace=workspace,
                    question=card["question"],
                    answer=card["answer"]
                )

            return redirect(
                "workspace_detail",
                workspace_id=workspace.id
            )

    else:

        form = FlashcardGeneratorForm()

    return render(
        request,
        "workspace/generate_flashcards.html",
        {
            "form": form,
            "workspace": workspace
        }
    )


@login_required
def delete_flashcard(request, card_id):

    card = get_object_or_404(
        Flashcard,
        id=card_id
    )

    workspace_id = card.workspace.id

    card.delete()

    return redirect(
        "workspace_detail",
        workspace_id=workspace_id
    )


@login_required
def check_quiz_answer(request, card_id):

    card = get_object_or_404(
        Flashcard,
        id=card_id
    )

    user_answer = request.POST.get(
        'answer',
        ''
    ).strip()

    correct = (
        user_answer.lower()
        in card.answer.lower()
    )

    return render(
        request,
        'workspace/quiz_result.html',
        {
            'card': card,
            'user_answer': user_answer,
            'correct': correct
        }
    )


@login_required
def flashcard_quiz(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    flashcards = Flashcard.objects.filter(
        workspace=workspace
    )

    if not flashcards.exists():

        return render(
            request,
            'workspace/quiz.html',
            {
                'error': 'No flashcards available.'
            }
        )

    card = choice(list(flashcards))

    return render(
        request,
        'workspace/quiz.html',
        {
            'card': card,
            'workspace': workspace
        }
    )
