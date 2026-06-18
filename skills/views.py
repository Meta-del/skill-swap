from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import UserSkillForm
from .models import UserSkill


@login_required
def explore_view(request):

    user = request.user

    matches = []

    my_learning = UserSkill.objects.filter(
        user=user,
        skill_type='learn'
    ).values_list('skill', flat=True)

    my_teaching = UserSkill.objects.filter(
        user=user,
        skill_type='teach'
    ).values_list('skill', flat=True)

    matches.extend(
        UserSkill.objects.filter(
            skill__in=my_learning,
            skill_type='teach'
        ).exclude(user=user)
    )

    matches.extend(
        UserSkill.objects.filter(
            skill__in=my_teaching,
            skill_type='learn'
        ).exclude(user=user)
    )

    return render(
        request,
        'skills/explore.html',
        {
            'matches': matches
        }
    )
    query = request.GET.get('q')

    if query:

        users = UserSkill.objects.filter(
            Q(skill__name__icontains=query)
            |
            Q(skill__category__icontains=query)
        )

    else:

        users = UserSkill.objects.all()


@login_required
def add_skill(request):

    if request.method == 'POST':

        print("POST DATA:", request.POST)

        form = UserSkillForm(request.POST)

        if form.is_valid():

            print("FORM IS VALID")

            user_skill = form.save(commit=False)
            user_skill.user = request.user
            user_skill.save()

            print("SKILL SAVED")

            return redirect('profile')

        else:

            print("FORM ERRORS:")
            print(form.errors)

    else:

        form = UserSkillForm()

    return render(
        request,
        'skills/add_skill.html',
        {
            'form': form
        }
    )


@login_required
def edit_skills(request):

    if request.method == 'POST':

        form = UserSkillForm(request.POST)

        if form.is_valid():

            UserSkill.objects.filter(
                user=request.user
            ).delete()

            for skill in form.cleaned_data['skills']:

                UserSkill.objects.create(
                    user=request.user,
                    skill=skill
                )

            return redirect('profile')

    else:

        form = UserSkillForm()

    return render(
        request,
        'skills/add_skills.html',
        {
            'form': form
        }
    )


@login_required
def recommendations(request):

    my_skills = UserSkill.objects.filter(
        user=request.user
    )

    recommendations = UserSkill.objects.exclude(
        user=request.user
    )

    return render(
        request,
        'skills/recommendations.html',
        {
            'recommendations': recommendations
        }
    )
