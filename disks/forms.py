from django import forms
from .models import *

class Recherche(forms.Form):
    title = forms.CharField(max_length= 250)
    def clean(self):
        cleaned_data = super(Recherche, self).clean()
        title = cleaned_data.get("title")
        return cleaned_data

class AlbumForm(forms.ModelForm):
        class Meta:
            model = Album
            fields = "__all__"

#On peut rajouter une fonction def clean(self) pour s'assurer que l'album crée n'existe pas déja.
