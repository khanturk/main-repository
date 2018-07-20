from django.contrib import admin

from .models import Pazar, Bolum,Reyon,UrunAdi,UrunTipi,UrunOzellikleri

admin.site.register(Pazar)
admin.site.register(Bolum)
admin.site.register(Reyon)
admin.site.register(UrunAdi)
admin.site.register(UrunOzellikleri)
admin.site.register(UrunTipi)