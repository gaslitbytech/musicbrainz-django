""" forms """

from django import forms

from .models import ArtistSearch


class ArtistSearchForm(forms.ModelForm):
    """Form validator for Artist Search"""

    class Meta:
        model = ArtistSearch
        fields = ("artist", "country")
        # exclude = ('gender', )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
