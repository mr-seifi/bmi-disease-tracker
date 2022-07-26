from django.db import models
from .enums import SexChoices
from django.contrib.auth.models import User


class Person(User):
    age = models.IntegerField(verbose_name='Age')
    sex = models.CharField(max_length=8, choices=SexChoices.choices, verbose_name='Sex')
    height = models.FloatField(verbose_name='Height in cm')
    weight = models.FloatField(verbose_name='Weight in Kg')
