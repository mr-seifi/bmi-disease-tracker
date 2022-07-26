from bio.services import BloodTestService
from bio.models import BloodTest
from celery import shared_task


@shared_task()
def get_blood_test_result():
    service = BloodTestService()
    unchecked_blood_tests = BloodTest.objects.filter(result__isnull=True)

    to_update = []
    for blood_test in unchecked_blood_tests:
        blood_test.result = service.predict(model=blood_test)
        to_update.append(blood_test)

    BloodTest.objects.bulk_update(to_update, fields=['result'])
