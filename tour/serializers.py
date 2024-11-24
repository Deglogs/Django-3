from rest_framework import serializers
from django.conf import settings
from .models import Tours,Booking,Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=settings.AUTH_USER_MODEL
        fieds=['id','username','email','role']
        read_only_fields=['id']


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tours
        fields=['Tour_id','Name','TDate','Location']
        read_only_fields=['Tour_id']

class BookingSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    booked_for=TourSerializer(read_only=True)

    class Meta:
        model=Booking
        fields=['Booking_id','BDate','Payment_Type','user','booked_for']
        read_only_fields=['Booking_id']

class ReviewSerializer(serializers.ModelSerializer):
    written_by=UserSerializer(read_only=True)
    regarding=TourSerializer(read_only=True)

    class Meta:
        model=Review
        fields=['Review_id','rating','comment','written_by','regarding']
        read_only_fields=['Review_id']
        