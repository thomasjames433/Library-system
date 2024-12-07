from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password','email','reg_date','membership']
        extra_kwargs={
            'password':{'write_only':True},
            'username': {'required': True},  # Make username required
            'email': {'required': True},  
        }

    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
    
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']
