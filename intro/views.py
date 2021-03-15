from django.shortcuts import render


# Create your views here.
#<img id="display-my-image" src={% static 'images/arunkumar_web_img.jpg' %}/>
def intro(request):
    return render(request,'home.html')