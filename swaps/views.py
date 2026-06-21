from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from workspace.models import Workspace, Goal
from .models import SwapRequest
from skills.models import UserSkill

from workspace.models import Notification
from django.contrib import messages


@login_required
def send_request(request, skill_id):

    match = get_object_or_404(
        UserSkill,
        id=skill_id
    )

    SwapRequest.objects.create(
        sender=request.user,
        receiver=match.user,
        skill=match.skill
    )
    messages.success(
        request,
        "Swap request sent successfully!"
    )

    Notification.objects.create(
        user=match.user,
        message=f"{request.user.username} sent you a swap request"
    )

    return redirect('explore')


@login_required
def inbox(request):

    requests = SwapRequest.objects.filter(
        receiver=request.user
    ).order_by('-created_at')

    return render(
        request,
        'swaps/inbox.html',
        {
            'requests': requests
        }
    )


@login_required
def accept_request(request, request_id):

    swap = get_object_or_404(
        SwapRequest,
        id=request_id,
        receiver=request.user
    )

    swap.status = 'accepted'
    swap.save()
    workspace, created = Workspace.objects.get_or_create(
        swap_request=swap
    )
    Goal.objects.get_or_create(
        workspace=workspace,
        title='Complete Introduction'
    )

    Goal.objects.get_or_create(
        workspace=workspace,
        title='Finish Beginner Topics'
    )

    Goal.objects.get_or_create(
        workspace=workspace,
        title='Complete Final Practice'
    )
    Notification.objects.create(
        user=swap.sender,
        message=f"{swap.receiver.username} accepted your request"
    )

    return redirect(
        'workspace_detail',
        workspace_id=workspace.id
    )


@login_required
def reject_request(request, request_id):

    swap = get_object_or_404(
        SwapRequest,
        id=request_id
    )

    swap.status = 'rejected'
    swap.save()

    return redirect('inbox')


@login_required
def add_flashcard(request, workspace_id):

    workspace = get_object_or_404(
        Workspace,
        id=workspace_id
    )

    if request.method == 'POST':

        form = FlashcardForm(request.POST)

        if form.is_valid():

            flashcard = form.save(
                commit=False
            )

            flashcard.workspace = workspace

            flashcard.save()

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
            'form': form,
            'workspace': workspace
        }
    )
