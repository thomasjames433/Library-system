# {
#   "username":"hi",
#   "password":"hi",
#   "email":"hi@gmail.com",
#   "membership":"regular"
# }


# {
#   "title":"The Great Gatsby",
#   "author":"F. Scott Fitzgerald",
#   "published_year":1925,
#   "genre":"Fiction",
#   "available_copies":5
  
# }

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

# from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from rest_framework import generics

from rest_framework_simplejwt.tokens import RefreshToken    
# @csrf_exempt
class UserRegistration(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'message':"Something Went Wrong", 'errors':serializer.errors})
        
        serializer.save()

        user=User.objects.get(username=serializer.data['username'])
        
        refresh=RefreshToken.for_user(user)

        return Response({'status':200, 'payload':serializer.data, 'refresh':str(refresh), 'access':str(refresh.access_token), 'message':'User Registered'})

class UserLogin(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user is None:
            return Response({'status':401,'message':"Invalid Credentials"})
        
        refresh= RefreshToken.for_user(user)
        return Response({'status':200, 'payload':user.username ,'refresh':str(refresh), 'access':str(refresh.access_token), 'message':'Login Succesful'})

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAdminorSafe1(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        return request.user and request.user.is_authenticated and request.user.is_staff

class IsAdminorSafe2(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated and request.user.is_staff
    

class BookListAdd(generics.CreateAPIView,generics.ListAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminorSafe2]
    
    queryset=Book.objects.all()

    def get_serializer_class(self):
        if self.request.method=='GET':  
            return BookListSerializer
        return BookSerializer


class BookViewUpdateDelete(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminorSafe1]
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    lookup_field='id'

class UserView(generics.CreateAPIView,generics.ListAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]

    queryset= User.objects.all()
    serializer_class=UserViewSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        
        
        user.set_password(serializer.validated_data['password'])
        
        user.save()

from django.contrib.auth.hashers import make_password

class IsAdminorUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and (request.user.is_superuser or request.user.is_staff):
            return True
        
        if view.kwargs.get('username') and request.user.username == view.kwargs.get('username'):
            return True
        
        return False

class UserUpdate(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminorUser]
    queryset=User.objects.all()
    serializer_class=UserUpRetDel
    lookup_field='username'

    def perform_update(self, serializer):
        password=serializer.validated_data.get('password')

        if password:
            serializer.validated_data['password'] = make_password(password)
        
        serializer.save()