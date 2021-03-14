from django import forms
from django.forms import fields
from .models import Played

class PlayedForm(forms.ModelForm):
    class Meta:
        model = Played
        fields = ['date', 'maintenance']
