from django.db import models

from django.db import models
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('Language', 'Language'),
        ('Business', 'Business'),
        ('Design', 'Design'),
    ]

    name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Programming'
    )

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    TEACH = 'teach'
    LEARN = 'learn'

    TYPE_CHOICES = [
        (TEACH, 'Teach'),
        (LEARN, 'Learn'),
    ]

    skill_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"
