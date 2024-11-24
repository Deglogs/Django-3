from django.contrib import admin
from django.urls import path,include
import tour.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(tour.urls)),
]
