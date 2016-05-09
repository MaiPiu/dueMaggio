from django.contrib import admin
from gestione.models import *
from django import forms

# admin.autodiscover()
#class DestinatariInline(admin.TabularInline):
 #   model = DestinatA
  #  extra = 2

#class CircolariOption(admin.ModelAdmin):
 #   inlines = [DestinatariInline]
    
admin.site.register(Pizza)
admin.site.register(Farina)
admin.site.register(Ordine)
admin.site.register(Dettaglio)
# admin.site.register(Libro)
#admin.site.register(Libro,LibroOption)