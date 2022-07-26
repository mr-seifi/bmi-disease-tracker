from django.db import models
from account.models import Person
from .enums import DailyActivityChoices, BloodTypeChoices


class InTimeBio(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    country = models.CharField(max_length=8, verbose_name='Country')
    smoker = models.BooleanField(default=False, verbose_name='Smoker?')
    hip = models.FloatField(default=100, verbose_name='Hip in cm')
    waist = models.FloatField(default=110, verbose_name='Waist in cm')
    wrist = models.FloatField(default=20, verbose_name='Wrist in cm')
    neck = models.FloatField(default=40, verbose_name='Neck in cm')
    current_heart_rate = models.FloatField(default=60, verbose_name='Current Heart Rate in bpm')
    daily_activity_level = models.CharField(max_length=8, choices=DailyActivityChoices.choices,
                                            default=DailyActivityChoices.M, verbose_name='Daily Activity')
    blood_pressure_sys = models.FloatField(default=120, verbose_name='Sys Blood Pressure in mmHg')
    blood_pressure_dia = models.FloatField(default=80, verbose_name='Dia Blood Pressure in mmHg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BloodTest(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    urea = models.FloatField(verbose_name='Urea')
    cr = models.IntegerField(verbose_name='Creatinine')
    hba1c = models.FloatField(verbose_name='Hemoglobin A1C')
    chol = models.FloatField(verbose_name='Cholesterol')
    tg = models.FloatField(verbose_name='Triglycerides')
    hdl = models.FloatField(verbose_name='High-density lipoproteins')
    ldl = models.FloatField(verbose_name='Low-density lipoproteins')
    vldl = models.FloatField(verbose_name='Very Low-density lipoproteins')
    result = models.CharField(null=True, max_length=2, verbose_name='Blood Test Result')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Recommendation(models.Model):
    blood_type = models.CharField(max_length=5, choices=BloodTypeChoices.choices)
    recommendation = models.TextField(verbose_name='Recommendation')
