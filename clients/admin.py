from django.contrib import admin

# Register your models here.
# on import les differents models afin de pouvoir les utiliser
from . models import *


class ClientAdmin(admin.ModelAdmin):
    
    search_fields = ('client',)
    list_display=('client',)
    list_filter = ('client',)

class AchatAdmin(admin.ModelAdmin):
    
    search_fields = ('produit',)
    list_display=('produit','prix',)
    list_filter = ('prix',)

admin.site.register(Achat,AchatAdmin)
admin.site.register(Client,ClientAdmin)
