from django import forms
from .models import UserSkill, Skill


class UserSkillForm(forms.Form):

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
