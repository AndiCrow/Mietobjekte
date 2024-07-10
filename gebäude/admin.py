from django.contrib import admin
from .models import Objekte, Kosten, Mietern, Technik
# Register your models here.

admin.site.register(Objekte)
admin.site.register(Kosten)
admin.site.register(Mietern)
admin.site.register(Technik)
