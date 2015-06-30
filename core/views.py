from django.shortcuts import render
from permissions import IsAuthenticatedOrCreate
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer,SignUpSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SignUp(generics.CreateAPIView):
    
    serializer_class = SignUpSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user=User(username=serializer.data['username'],
                      first_name=serializer.data['first_name'],
                      last_name=serializer.data['last_name'],
                      email=serializer.data['email'])
            user.set_password(serializer.data['password'])
            user.save()
            return Response(serializer.validated_data)

        return Response(serializer.errors)	

