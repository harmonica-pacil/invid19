from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from dataCovid.models import Krisan

class KrisanForm(forms.ModelForm) :
    class Meta :
        model = Krisan
        fields = ['text_krisan']

    error_messages = {
        'required' : 'Harap isi kotak kritik dan saran.'
    }

    text_krisan = forms.CharField(label = "Kritik dan Saran", required = True,
    widget = forms.Textarea(attrs= {'type' : 'text', 'placeholder' : 'Silakan tulis kritik dan saran Anda terhadap fitur Data Covid-19 kami.'}))