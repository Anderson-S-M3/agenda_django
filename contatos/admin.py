from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'email', 'telefone', 'categoria', 'ocultar')
    list_display_links = ('nome', 'sobrenome')
    list_editable = ('telefone', 'ocultar')

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
