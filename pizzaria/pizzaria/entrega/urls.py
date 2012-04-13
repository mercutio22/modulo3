from django.conf.urls import patterns, include, url

from .views import hora_atual, pizzas_pendentes, HoraView, cadastro, cliente_obs
from django.views.generic import ListView, DetailView
from .models import Pizza, Cliente

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^pizzaria/', include('pizzaria.foo.urls')),
    url(r'hora$', HoraView.as_view(), name='hora'),
    #url(r'pizzas$', pizzas_pendentes, name='pizzas_pendentes'), 
    url(r'pizzas$',ListView.as_view(queryset=Pizza.objects.order_by('pedido'), context_object_name='lista'), name='pizzas'),
    url(r'clientes$', ListView.as_view(model=Cliente, context_object_name='clientes'), name='lista-clientes'),
    url(r'cliente/(?P<pk>\d+)$', 
        DetailView.as_view(model=Cliente, context_object_name='cliente'), 
        name='ficha-cliente'),
    url(r'novocli$', cadastro, name='cadastro-novo'),
    url(r'cliente-obs$', cliente_obs, name='cliente-obs')
)
