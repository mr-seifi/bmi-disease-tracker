from django.db.models import TextChoices


class DailyActivityChoices(TextChoices):
    L = 'low', 'L'
    M = 'medium', 'M'
    H = 'high', 'H'


class BloodTypeChoices(TextChoices):
    y = 'Y', 'Y'
    n = 'N', 'N'
    p = 'P', 'P'
