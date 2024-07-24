from django.urls import path
from .views import ObjekteView, objektes, details, wohnungen_details, wohnung_details
from gebäude import views 

urlpatterns = [
    path('', ObjekteView.as_view(), name='objekte-list'),
    path('objekte/', objektes, name='objekte'),
    path('objekte/<int:id>', details, name='details'),
    path('wohnungen/<int:id>/', wohnungen_details, name='wohnungen'),
    path('wohnung/<int:id>/', wohnung_details, name='wohnung-details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('objekt/neu/', views.eintragen_objekte, name='objekt_erstellen'),
    path('kosten/neu/', views.eintragen_kosten, name='kosten_erstellen'),
    path('technik/neu/', views.eintragen_technik, name='technik_erstellen'),
    path('mietern/neu/', views.eintragen_mieter, name='mietern_erstellen'),
]
