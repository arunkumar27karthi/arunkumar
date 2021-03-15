from django.urls import path
from numberDetection import views

urlpatterns = [
    path('numberDetection/', views.numberDetection, name='detect number'),
]
