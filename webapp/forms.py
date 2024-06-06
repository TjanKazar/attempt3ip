from django import forms
from .models import Prijavnica  

class PrijavaForm(forms.ModelForm):
    class Meta:
        model = Prijavnica
        fields = ['ime', 'priimek', 'email', 'phone', 'dejavnost', 'datumrojstva', 'valid', 'komentar']