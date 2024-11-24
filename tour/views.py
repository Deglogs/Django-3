from django.shortcuts import render
from .serializers import *
from .models import Tours,Booking,Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])

def TourView(request):
    app=Tours.objects.all()
    serializer = TourSerializer(app,many=True)
    return Response(serializer.data)