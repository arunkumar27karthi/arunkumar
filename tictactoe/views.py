from django.shortcuts import render

# Create your views here.

def playgame(request):
    return render(request,'game.html')