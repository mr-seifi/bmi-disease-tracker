from rest_framework import generics
from account.models import Person
from account.serializers import PersonSignupSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class PersonSignupCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSignupSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )
