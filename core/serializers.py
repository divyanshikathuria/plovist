from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.core.validators import RegexValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SignUpSerializer(serializers.ModelSerializer):
    
   
    password = serializers.CharField(write_only=True, required=False)
    #confirm_password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ( 'username','first_name','last_name','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
         
        password = validated_data.get('password', None)
        #confirm_password = validated_data['confirm_password']

        #if password and confirm_password and password == confirm_password:
        user.set_password(password)
        user.save()
        
        return user

     
           
