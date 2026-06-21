from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from skills.models import Skill, UserSkill


class RegisterForm(UserCreationForm):
    teach_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    learn_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'bio',
            'location',
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)


        if commit:
            teach_skills = self.cleaned_data.get('teach_skills')
            learn_skills = self.cleaned_data.get('learn_skills')

            if teach_skills:
                for skill in teach_skills:
                    UserSkill.objects.create(
                        user=user,
                        skill=skill,
                        skill_type='teach'
                    )

            if learn_skills:
                for skill in learn_skills:
                    UserSkill.objects.create(
                        user=user,
                        skill=skill,
                        skill_type='learn'
                    )

        return user
