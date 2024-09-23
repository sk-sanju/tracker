from django.urls import path
from .views import track

urlpatterns = [
    path('', track, name= 'tracker'),
]