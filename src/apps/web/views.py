from django.shortcuts import render
from .models import Photo
# Create your views here.


def home(request):
    imagenes = Photo.objects.all()
    return render(request, 'web/home.html', locals())





