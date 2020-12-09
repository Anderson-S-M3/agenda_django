from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('usuario','nome','sobrenome', 'email', 'telefone', 'categoria', 'mostrar')
    list_display_links = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
