from django import forms
from .models import Objekte, Kosten, Technik, Mietern


class ObjekteForm(forms.ModelForm):
    class Meta:
        model = Objekte
        fields = ['name', 'address']


class KostenForm(forms.ModelForm):
    class Meta:
        model = Kosten
        fields = ['objekte', 'kosten', 'einnahmen', 'von_wem', 'Datum', 'Dokument']


class TechnikForm(forms.ModelForm):
    class Meta:
        model = Technik
        fields = ['objekt', 'gegenstand', 'wohnung']


class MieternForm(forms.ModelForm):
    class Meta:
       model = Mietern
       fields = ['objekt', 'vornanme', 'nachname', 'monats_miethe', 'kaution']

 
