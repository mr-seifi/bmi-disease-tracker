from django.urls import path
from .views import PersonSignupCreateAPIView


urlpatterns = [
    path('signup/', PersonSignupCreateAPIView.as_view())
]
