from django.urls import path,include
from tictactoe import views

urlpatterns = [
    path('tictactoe/', views.playgame, name='tictactoe'),
]
