from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SignUpSerializer(serializers.ModelSerializer):
    
   
    password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'})
    
    
    class Meta:
        model = User
        fields = ( 'username','first_name','last_name','email', 'password','confirm_password')
    
    def validate(self, attrs):
        attrs = super(SignUpSerializer, self).validate(attrs)
        if attrs['confirm_password'] != attrs['password']:
            raise serializers.ValidationError('Passwords do not match.')
        return attrs
    
    
        
        

           
