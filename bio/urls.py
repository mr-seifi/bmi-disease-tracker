from django.urls import path
from .views import BloodTestListCreateAPIView


urlpatterns = [
    path('bloodtest/', BloodTestListCreateAPIView.as_view())
]
