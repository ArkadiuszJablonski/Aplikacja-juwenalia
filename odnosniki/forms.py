from django import forms
from .models import Odnosnik


class OdnosnikForm(forms.ModelForm):
    class Meta:
        model = Odnosnik
        fields = ['nazwa', 'link', 'zdjecie']
        