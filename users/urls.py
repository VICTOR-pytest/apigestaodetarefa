from django.urls import path
from .views import UserCreateView
from django.urls import path
from .views import test_view



urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path("test/", test_view),
]
