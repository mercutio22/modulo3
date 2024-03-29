#coding=utf8
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
import datetime
from pizzaria.entrega.models import Pizza
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ClienteModelForm, ObservacaoClienteForm

class HoraView(TemplateView):
    template_name = 'entrega/hora.html'
    
    def get_context_data(self, **kwargs ):
        context = super(HoraView, self).get_context_data(**kwargs)
        context['hora_certa'] = datetime.datetime.now()
        return context

def hora_atual(request):
    agora = datetime.datetime.now()
    html = u'<html><body> Hora atual: {0}</body></html>'.format(agora)
    return HttpResponse(html)
    
def pizzas_pendentes_na_unha(request):
    listagem = []
    for pizza in Pizza.objects.order_by('pedido_id'):
        listagem.append(unicode(pizza))
    html = u'<html><body><h1> Pizzas pendentes </h1>'
    html += u'<pre>{0}</pre></body></html>'.format(',\n'.join(listagem))
    return HttpResponse(html)
    
def pizzas_pendentes(request):
    lista_de_pizzas = Pizza.objects.all()
    return render(request, 'entrega/pizzas.html',
                  {'lista': lista_de_pizzas},
                  content_type='text/html')

from django.core.urlresolvers import reverse
def cadastro(request):
    if request.method == 'POST':
        formulario = ClienteModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #TODO:usar reverse url ao invés de url amarrada
            return HttpResponseRedirect(reverse('lista-clientes'))
    else:
        formulario = ClienteModelForm()
    return render(request, 'entrega/cadastro.html',
          {'formulario': formulario},
          )
          
def cliente_obs(request):
    if request.method == 'POST':
        formulario = ObservacaoClienteObs(request.POST)
        if formulario.is_valid():
            cliente_id = request.POST.get('cliente_id')
            cliente = Cliente.objects.get(pk='cliente_id')
            cliente_obs = formulario.cleaned_data['obs']
            cliente.save()
    return HttpResponseRedirect(reverse('ficha-cli'))
                
