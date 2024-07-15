from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Objekte, Kosten, Mietern, Technik
from .serializer import ObjekteSerializer
from django.shortcuts import render, get_object_or_404
from django.db import models
import pandas as pd

class ObjekteView(APIView):
    def get(self, request):
        objekte = Objekte.objects.all()
        serializer = ObjekteSerializer(objekte, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ObjekteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def objektes(request):

    objekte = Objekte.objects.all()

    return render(request, 'test.html', {'objekte': objekte})

def base(request):

    objekte = Objekte.objects.all()

    return render(request, 'base.html', {'objekte': objekte})



def details(request, id):
    objekte = Objekte.objects.all()
    objekt = get_object_or_404(Objekte, id=id)
    kosten = objekt.kosten_set.all()
    mietern = Mietern.objects.filter(objekt=objekt)
    technik = Technik.objects.filter(objekt=objekt)
    wohnungen = mietern.values_list('wohnung', flat=True).distinct()
    gesamtsumme_miete = mietern.aggregate(total=models.Sum('monats_miethe'))['total']
    gesamtsumme_kaution = mietern.aggregate(total=models.Sum('kaution'))['total']
    gesamtsumme_kosten = kosten.aggregate(total=models.Sum('kosten'))['total']
    
    if gesamtsumme_miete is None:
        gesamtsumme_miete = 0
    if gesamtsumme_kosten is None:
        gesamtsumme_kosten = 0

    gewinn_verlust = gesamtsumme_miete - gesamtsumme_kosten

    return render(request, 'test_details.html', {
        'objekt': objekt,
        'kosten': kosten,
        'technik': technik,
        'mietern': mietern,
        'wohnungen': wohnungen,
        'gesamtsumme_miete': gesamtsumme_miete,
        'gesamtsumme_kaution': gesamtsumme_kaution,
        'gesamtsumme_kosten':gesamtsumme_kosten,
        'gewinn_verlust': gewinn_verlust,
        'objekte': objekte})


def wohnungen_details(request, id):
    objekt = get_object_or_404(Objekte, id=id)
    mietern = Mietern.objects.filter(objekt=objekt)
    technik = Technik.objects.filter(objekt=objekt)

    wohnungen = mietern.values_list('wohnung', flat=True).distinct()

    return render(request, 'technik.html', {'objekt': objekt,'mietern':mietern, 'technik':technik, 'wohnungen':wohnungen})

def wohnung_details(request, id):
    mieter = get_object_or_404(Mietern, id=id)
    technik = Technik.objects.filter(objekt=mieter.objekt, wohnung=mieter.wohnung)
    objekte = Objekte.objects.all()
    return render(request, 'wohnung_details.html', {'mieter': mieter, 'technik': technik, 'objekte': objekte})


def dashboard(request):

    objekte = Objekte.objects.all()
    mietern = Mietern.objects.all()
    technik = Technik.objects.all()
    kosten = Kosten.objects.all()

    mietern_df = pd.DataFrame(list(mietern.values()))
    kosten_df = pd.DataFrame(list(kosten.values()))

    gesamtsumme_miete = mietern_df['monats_miethe'].sum() if not mietern_df.empty else 0
    gesamtsumme_kosten = kosten_df['kosten'].sum() if not kosten_df.empty else 0
    gewinn_verlust = gesamtsumme_miete - gesamtsumme_kosten

    import plotly.express as px

    data = {
        'Category': ['Gesamtsumme Miete', 'Gesamtsumme Kosten'],
        'Amount': [gesamtsumme_miete, gesamtsumme_kosten]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Category', y='Amount', title='Finanzübersicht')
    chart = fig.to_html(full_html=False)

    context = {
        'objekte': objekte,
        'mietern': mietern,
        'technik': technik,
        'kosten': kosten,
        'gesamtsumme_miete': gesamtsumme_miete,
        'gesamtsumme_kosten': gesamtsumme_kosten,
        'gewinn_verlust': gewinn_verlust,
        'chart': chart,
    }
    return render(request, 'dashboard.html', context)