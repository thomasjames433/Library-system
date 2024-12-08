from django.urls import path,include

from .views import *

urlpatterns=[
    path('api/auth/register',UserRegistration.as_view(),name='user_register'),
    path('api/auth/login',UserLogin.as_view(),name='user_login'),
    
    path('api/books',BookListAdd.as_view(),name='booklistadd'),
    path('api/books/<id>',BookViewUpdateDelete.as_view(),name='bookviewupdatedelete'),
    path('api/users',UserView.as_view(),name='viewusers'),
    path('api/users/<str:username>',UserUpdate.as_view(),name='updateusers'),
]