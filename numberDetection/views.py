from django.shortcuts import render


# Create your views here.
#<img id="display-my-image" src={% static 'images/arunkumar_web_img.jpg' %}/>
def numberDetection(request):

    import cv2
    import matplotlib.pyplot as plt
    import numpy as np
    from tensorflow.keras.models import load_model
    later = load_model('C:/Users/arunkumar/Downloads/numbers_det.h5')
    img = cv2.imread('test.jpg',1)
    img1=img/255.0
    img1=np.reshape(img1,(1,32,32,3))
    plt.figure()

    plt.imshow(img)

    name=later.predict_classes(img1)
    print(name[0])
    plt.xlabel(name[0])

    number = 999;
    return render(request,'numberDetection.html',{'detectedNum': number })