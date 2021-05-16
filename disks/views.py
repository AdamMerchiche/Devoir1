from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import Recherche

# Create your views here.
def lire_albums (request):
    albums = Album.objects.all()
    return render(request, 'disks/accueil.html', {'albums':Album.objects.all()})

def afficher_tracks(request, album_id):
    return render(request, 'disks/afficher_tracks.html', {'tracks': Track.objects.filter(album_id =album_id)})

def afficher_recherche(request):
    requete = request.GET.get('requete')
    if not requete:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=requete)
    return render(request, 'disks/recherche.html', {'albums' : albums})
