from django.forms import ModelForm
from django.forms import Textarea
from .models import FeedbackMessage
from django import forms

class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ['name', 'lastname', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 71, 'border': None} )
        }