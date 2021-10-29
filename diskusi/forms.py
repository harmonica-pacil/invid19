from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = [
            'title',
            'message'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': "title_input", 'placeholder': "Put your title here ..."}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': "message_input", 'placeholder': "Write your message ..."}),
        }