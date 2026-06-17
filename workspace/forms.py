from django import forms
from .models import Goal, Lesson, Material, Message, Review, Flashcard
from .models import Review


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ['title']


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = [
            'title',
            'scheduled_date',
            'scheduled_time',
            'meeting_link'
        ]


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = [
            'title',
            'file'
        ]


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['text']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            'rating',
            'comment'
        ]


class FlashcardForm(forms.ModelForm):

    class Meta:

        model = Flashcard

        fields = [
            'question',
            'answer'
        ]
