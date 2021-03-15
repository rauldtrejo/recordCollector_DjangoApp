from django import forms
from django.forms import fields
from .models import Played, Record, CleaningBrush

class PlayedForm(forms.ModelForm):
    class Meta:
        model = Played
        fields = ['date', 'maintenance']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name','artist','format','description','genre','released']

class CleaningForm(forms.ModelForm):
    class Meta:
        model = CleaningBrush
        fields = ['brand', 'name']