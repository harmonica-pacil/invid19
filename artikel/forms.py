from django import forms
from .models import Artikel


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields ='__all__'