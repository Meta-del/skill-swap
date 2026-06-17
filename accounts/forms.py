from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from skills.models import Skill
from django import forms


class RegisterForm(UserCreationForm):

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

    def save(self, commit=True):

        user = super().save(commit)

        from skills.models import UserSkill

        for skill in self.cleaned_data['teach_skills']:

            UserSkill.objects.create(
                user=user,
                skill=skill
            )

        return user
