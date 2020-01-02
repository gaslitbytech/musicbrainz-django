from django import forms
from .models import MapBoundView


class BookForm(forms.ModelForm):
    class Meta:
        model = MapBoundView
        fields = ('north', 'south', 'east', 'west', 'zoom')
