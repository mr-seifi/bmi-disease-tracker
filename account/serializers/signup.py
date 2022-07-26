from rest_framework import serializers
from account.models import Person
from rest_framework.authtoken.models import Token


class PersonSignupSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(instance):
        tk = Token.objects.create(user=instance)
        return tk.key

    class Meta:
        model = Person
        fields = ('email', 'password', 'first_name', 'last_name', 'age', 'sex', 'weight', 'height', 'token')
