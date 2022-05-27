from django import forms
from .models import LostItem


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['nazwa', 'opis', 'kontakt', 'zdjecie']
        