
from rest_framework.authtoken import views as rest_views

from django.urls import path

from .views import CustomAuthToken, RegisterView


urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view(), name="")
]