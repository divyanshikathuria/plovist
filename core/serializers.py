from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from models import UserProfile

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
    terms = serializers.BooleanField(label="I agree to the Terms & Conditions")
    
    class Meta:
        model = User
        fields = ( 'username','email', 'password','confirm_password','terms')
    
    def validate(self, attrs):
        attrs = super(SignUpSerializer, self).validate(attrs)
        if attrs['confirm_password'] != attrs['password']:
            raise serializers.ValidationError('Passwords do not match.')
        if attrs['terms']==False:
            raise serializers.ValidationError('You must accept the Terms And Conditions.')
        return attrs
    

        
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields= ( 'user','name', 'about', 'location','picture', 'website', 'open_for_design', 
        	       'phone_number', 'profile_scores','profile_social' )






    
        
        

           

