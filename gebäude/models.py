from django.db import models
from django.core.exceptions import ValidationError
import datetime


def zusässige_negative(value):
    if value >= 0 :
        raise ValidationError(
            '%(value)s ist keine negative Zahl',
            params={'value': value},
        )
def zusässige_posetive(value):
    if value <= 0:
        raise ValidationError(
            '%(value)s ist keine posetive Zahl',
            params={'value': value},
        )

class Objekte(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Kosten(models.Model):
    objekte = models.ForeignKey(Objekte, on_delete=models.CASCADE)
    kosten = models.IntegerField(blank=True, null=True)
    einnahmen = models.IntegerField(blank=True, null=True)
    #kosten = models.IntegerField(validators=[zusässige_negative], blank=True)
    #einnahmen = models.IntegerField(validators=[zusässige_posetive], blank=True)
    von_wem = models.CharField(max_length=150, blank=True)
    Datum = models.DateField(default= datetime.datetime.now)
    Dokument = models.ImageField(upload_to="dokument/", blank=True)

    def __str__(self):
         return f"Kosten für {self.objekte}"



class Technik(models.Model):
    objekt = models.ForeignKey(Objekte, on_delete=models.CASCADE)
    gegenstand = models.CharField(max_length=200)
    wohnung = models.CharField(max_length=200)


class Mietern(models.Model):
    objekt = models.ForeignKey(Objekte, on_delete=models.CASCADE)
    vornanme = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)
    monats_miethe = models.IntegerField(validators=[zusässige_posetive], blank=True)
    kaution = models.IntegerField(validators=[zusässige_posetive], blank=True)
    wohnung = models.IntegerField(blank=True, null=True)
