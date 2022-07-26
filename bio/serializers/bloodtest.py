from rest_framework import serializers
from bio.models import BloodTest, Recommendation
from rest_framework.authtoken.models import Token


class BloodTestSerializer(serializers.ModelSerializer):
    test_result = serializers.SerializerMethodField()
    recommendations = serializers.SerializerMethodField()

    @staticmethod
    def get_test_result(instance):
        if instance.result == 'Y':
            return 'You have an specific disease!'
        elif instance.result == 'N':
            return 'You don\'t have any specific disease!'
        return 'Wait for a doctor check!'

    @staticmethod
    def get_recommendations(instance):
        if not instance:
            return 'Null until a blood test result!'
        recommendations = \
            list(Recommendation.objects.filter(blood_type=instance.result).values_list('recommendation',
                                                                                       flat=True))
        return recommendations

    def create(self, validated_data):
        person = Token.objects.get(key=self.context['request'].auth).user
        validated_data['person_id'] = person.id
        return super(BloodTestSerializer, self).create(validated_data)

    class Meta:
        model = BloodTest
        fields = ('urea', 'cr', 'hba1c', 'chol', 'tg', 'hdl', 'ldl', 'vldl', 'test_result', 'recommendations')
