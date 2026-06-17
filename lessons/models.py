from django.db import models

from django.db import models
from django.conf import settings


class Lesson(models.Model):

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teaching_lessons'
    )

    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='learning_lessons'
    )

    topic = models.CharField(max_length=200)

    notes = models.TextField(blank=True)

    date = models.DateTimeField()

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
