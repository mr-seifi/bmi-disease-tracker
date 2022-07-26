from rest_framework import generics
from bio.models import BloodTest
from bio.serializers import BloodTestSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class BloodTestListCreateAPIView(generics.ListCreateAPIView):
    queryset = BloodTest.objects.all()
    serializer_class = BloodTestSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = Token.objects.get(key=self.request.auth).user
        queryset = BloodTest.objects.filter(person_id=user.id)
        return queryset
