from django.urls import path
from .views import request_token

urlpatterns = [
    path('request-token/', request_token, name='request_token'),
]
