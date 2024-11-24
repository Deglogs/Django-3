from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.conf import settings

class CustomUser(AbstractUser):
    username=None
    Role_Choices=(
        ('user','User'),
        ('tour_guide','Tour Guide'),
    )
    role=models.CharField(max_length=10,choices=Role_Choices,default='user')
    email=models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Tours(models.Model):
    Tour_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=25)
    TDate=models.DateField()
    Location=models.CharField(max_length=30)
    

class Booking(models.Model):
    Booking_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='bookings')
    booked_for=models.ForeignKey(Tours,on_delete=models.CASCADE,related_name='bookings')
    BDate=models.DateField()
    Payment_Type=models.CharField(max_length=30)

class Review(models.Model):
    Review_id=models.AutoField(primary_key=True)
    rating=models.IntegerField()
    comment=models.TextField()
    written_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reviews')
    regarding=models.ForeignKey(Tours,on_delete=models.CASCADE,related_name='reviews')
    