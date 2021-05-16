from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length = 250)
    artist_id = models.IntegerField()
    def __str__(self):
        return "{0} est dans l'album {1}".format(self.track, self.album)

class Album(models.Model):
    title = models.CharField(max_length= 250)
    artist = models.ForeignKey(Artist, on_delete= "models.CASCADE")
    def __str__(self):
        return self.title

class Track(models.Model):
    name = models.CharField(max_length = 250)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.IntegerField() #pas sur que ce soit une integer ici, plutot un décimal
    composer = models.CharField(max_length = 250)
    album = models.ForeignKey(Album, on_delete= "models.CASCADE")
    def __str__(self):
        return self.name

