from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.username


'''class Achievement(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=50,
        default='🏆'
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_mentor = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    experience = models.CharField(
        max_length=200,
        blank=True
    )

    hourly_availability = models.CharField(
        max_length=200,
        blank=True
    )
    rating = models.FloatField(
        default=0
    )
    bio = models.TextField(
        blank=True
    )
    achievements = models.ManyToManyField(
        Achievement,
        blank=True
    )'''
