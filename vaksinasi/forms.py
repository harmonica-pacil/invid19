from .models import Vaksin, Pendaftar
from django import forms
from django.forms import ModelForm


class VaksinForm(ModelForm):
    class Meta:
        model = Vaksin
        fields= '__all__'

class PendaftarForm(ModelForm):
    class Meta:
        model = Pendaftar
        fields= '__all__'
        