from django.urls import path
from .import views
from django.conf import settings


urlpattern=[
    path('',views.getdata),
    path('post/',views.postdata),
]