from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import JsonResponse

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



def test_view(request):
    return JsonResponse({"status": "API funcionando"})
