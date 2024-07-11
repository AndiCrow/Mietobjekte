from rest_framework import serializers
from .models import Objekte, Kosten, Technik, Mietern

class KostenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kosten
        fields = ['id', 'objekte', 'kosten', 'einnahmen', 'von_wem', 'Datum', 'Dokument']

class TechnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technik
        fields = ['id', 'objekt', 'gegenstand', 'wohnung']

class MieternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mietern
        fields = ['id', 'objekt', 'vornanme', 'nachname', 'monats_miethe', 'kaution']

class ObjekteSerializer(serializers.ModelSerializer):
    kosten_set = KostenSerializer(many=True, read_only=True)
    technik_set = TechnikSerializer(many=True, read_only=True)
    mietern_set = MieternSerializer(many=True, read_only=True)

    class Meta:
        model = Objekte
        fields = ['id', 'name', 'address', 'kosten_set', 'technik_set', 'mietern_set']
