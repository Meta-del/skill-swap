from django.db import models
from swaps.models import SwapRequest
from django.conf import settings


class Workspace(models.Model):

    swap_request = models.OneToOneField(
        SwapRequest,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Workspace {self.id}"


class Lesson(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    scheduled_date = models.DateField()

    scheduled_time = models.TimeField()

    meeting_link = models.URLField(
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )


class Material(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    file = models.FileField(
        upload_to='materials/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class Goal(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    completed = models.BooleanField(
        default=False
    )


class Message(models.Model):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    sent_at = models.DateTimeField(
        auto_now_add=True
    )


class Notification(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    message = models.CharField(
        max_length=255
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.message


class Review(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.rating} stars"


class Flashcard(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    question = models.CharField(
        max_length=255
    )
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='Medium'
    )
    times_correct = models.IntegerField(
        default=0
    )

    times_wrong = models.IntegerField(
        default=0
    )

    answer = models.TextField()

    def __str__(self):
        return self.question


'''class Summary(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )'''
