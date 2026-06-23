# from .models import Profile
from workspace.models import Notification
from skills.models import UserSkill
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def profile_view(request):

    skills = UserSkill.objects.filter(user=request.user)

    return render(request, 'accounts/profile.html', {
        'user_profile': request.user,
        'skills': skills
    })


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():

            user = form.save()

            return redirect('login')

        else:

            print(form.errors)

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


@login_required
def dashboard(request):

    from skills.models import UserSkill
    from swaps.models import SwapRequest
    from workspace.models import Workspace
    workspaces = Workspace.objects.filter(
        swap_request__sender=request.user
    ) | Workspace.objects.filter(
        swap_request__receiver=request.user
    )

    skills = UserSkill.objects.filter(user=request.user)

    received = SwapRequest.objects.filter(
        receiver=request.user
    )

    sent = SwapRequest.objects.filter(
        sender=request.user
    )

    return render(
        request,
        'accounts/dashboard.html',
        {
            'workspaces': workspaces
        }
    )


def mentors(request):

    mentors = UserSkill.objects.filter(
        skill_type='teach'
    ).select_related('user')

    return render(
        request,
        'accounts/mentors.html',
        {
            'mentors': mentors
        }
    )


@login_required
def notifications(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'accounts/notifications.html',
        {
            'notifications': notifications
        }
    )


def public_profile(request, user_id):

    User = get_user_model()
    profile_user = get_object_or_404(
        User,
        id=user_id
    )

    skills = UserSkill.objects.filter(
        user=profile_user
    )

    return render(
        request,
        'accounts/public_profile.html',
        {
            'profile_user': profile_user,
            'skills': skills
        }
    )
