from django.contrib import admin

# Register your models here.
# from . models import Zones, Corpuses
from . models import  Zone, Corpus, Agregat, Agregate, MaAgregate
    # Products, Pizza
    
admin.site.register(Agregat)
admin.site.register(Zone)
admin.site.register(Corpus)
admin.site.register(Agregate)
admin.site.register(MaAgregate)

# @admin.register(Agregat)
# class AgregatAdmin(admin.ModelAdmin):
#     # class Meta:
#     #     model = Agregat
#     list_display = ('n_zag', 'n_agr', 'n_zone')


