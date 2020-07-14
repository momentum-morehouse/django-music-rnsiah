from django.shortcuts import render
from .models import Album




def home(request):
  albums = Album.objects.all()
  return render(request, 'album/home.html', {'albums':albums})
