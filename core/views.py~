from django.shortcuts import render
from permissions import IsAuthenticatedOrCreate
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import redirect


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
                return redirect('/api-auth/login')
            return Response(serializer.validated_data)
         
        return Response(serializer.errors)	

class Profile(generics.RetrieveUpdateAPIView):

    """
    API endpoint that allows to retrieve and update Profile.
    """
    queryset = Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    def get_object(self,pk):
        
        return Profile.objects.get(id=pk)

    def get(self,request,pk):
    	profile = self.get_object(pk)
    	serializer = ProfileSerializer(profile)
    	return Response(serializer.data)

    def update(self, request,pk):
    	profile = self.get_object(pk)
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
