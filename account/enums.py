from django.db import models


class SexChoices(models.TextChoices):
    M = 'male', 'M'
    F = 'female', 'F'
