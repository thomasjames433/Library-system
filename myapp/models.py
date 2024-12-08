from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    membership_choices=(
        ('regular','Regular'),
        ('premium','Premium')
    )
    reg_date=models.DateField(auto_now_add=True)
    membership=models.CharField(max_length=10,choices=membership_choices,default='regular')

    email = models.EmailField(
        blank=False,  
        null=False,   
        help_text='A valid email address is required.'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user'
    )
    
    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title