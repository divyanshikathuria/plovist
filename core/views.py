from django.shortcuts import render
from permissions import IsAuthenticatedOrCreate
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import redirect
from rest_framework import status

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
    """
    API endpoint that registers new users.
    """
    
    serializer_class = SignUpSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    def create(self, request):
        registered= False
           
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user=User(username=serializer.data['username'],
                      email=serializer.data['email'])
            user.set_password(serializer.data['password'])
            user.save()
            registered = True
            def send_registration_confirmation(user):
	        subject = "Welcome Mail"
	        message = "Congratulations! Your Account is created."
	        send_mail(subject, message, 'admin@plovist.com', [user.email], fail_silently=True)
            obj = serializer.validated_data
            if registered==True:
                return redirect('/')
            return Response(serializer.validated_data)
         
        return Response(serializer.errors)	

'''class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of profile to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj[0] == self.request.user
'''

class Profile(generics.CreateAPIView):

    """
    API endpoint that allows to create profile.
    """
    
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    

  
class Profile_Update(generics.RetrieveUpdateAPIView):

    """
    API endpoint that allows to retrieve and update Profile.
    """
    
    
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        a=self.request.user
        return UserProfile.objects.filter(user__username=a)
