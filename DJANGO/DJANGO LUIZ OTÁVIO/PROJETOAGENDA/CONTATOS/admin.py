from django.contrib import admin
from . models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'mostrar')
    list_display_links = ('id', 'nome',)
    list_filter = ('nome', 'sobrenome',)
    list_per_page = 10
    search_field = ('nome')
    list_editable = ('mostrar',)

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

# Register your models here.
