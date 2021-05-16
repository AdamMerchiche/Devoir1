from django import forms
from .models import *

class Recherche(forms.Form):
    title = forms.CharField(max_length= 250)
    def clean(self):
        cleaned_data = super(Recherche, self).clean()
        title = cleaned_data.get("title")
        return cleaned_data

