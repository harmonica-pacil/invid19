from django import forms
from .models import Berita

class formBerita(forms.ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'