from models import Cliente, Pedido, Entregador
from django.contrib import admin


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'nome', 'endereco')
    list_display_links = list_display
    search_fields = ('fone', 'logradouro', 'email', 'nome')
    list_filter = ['logradouro']

class PedidoAdmin(admin.ModelAdmin):
    list_display= ('hora_inclusao', 'cliente', 'pronto', 'Partiu')
    
    def hora_inclusao(self, pedido):
        return pedido.inclusao.strftime('%H:%M')
    
    def Partiu(self, pedido):
        return bool(pedido.pronto and pedido.partida and pedido.entregador)
    Partiu.boolean = True
    



admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)
