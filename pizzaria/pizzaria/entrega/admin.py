from models import Cliente
from django.contrib import admin


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ('fone', 'logradouro', 'email', 'nome')
    list_filter = ['logradouro']


admin.site.register(Cliente,ClienteAdmin)
