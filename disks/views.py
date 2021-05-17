
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import Recherche

# Create your views here.
def lire_albums (request):
    albums = Album.objects.all()
    form = Recherche(request.GET or None)
    if form.is_valid():
        albums = Album.objects.filter(title__icontains=form.cleaned_data['title']) #Bien prendre la variable qu'on a instancié dans le form

    print(f"albums={albums}")
    return render(request, 'disks/accueil.html', {'albums' : albums, 'form':form})

def afficher_tracks(request, album_id):
    return render(request, 'disks/afficher_tracks.html', {'tracks': Track.objects.filter(album_id =album_id)})

def afficher_recherche(request):
    form = Recherche(request.GET or None)
    albums = Album.objects.all()
    if form.is_valid():
        albums = Album.objects.filter(title__icontains=form.cleaned_data['title'])
    return render(request, 'disks/recherche.html', {'albums': albums, 'form': form})
