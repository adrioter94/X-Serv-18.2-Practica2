from django.shortcuts import render
from models import URLS
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def Formulario(request):
    salida = ''
    url = ''
    formulario = '<form action="" method="POST">'
    formulario += 'Acortar url: <input type="text" name="valor">'
    formulario += '<input type="submit" value="Enviar">'
    formulario += '</form>'
    lista = URLS.objects.all()
    
    if request.method == 'POST':
        if request.POST['valor'].find('http') == -1:
            url = 'http://' + request.POST['valor']
        else:
            url = request.POST['valor']

        for fila in lista:
            if fila.url == url:
                return HttpResponse('La url ' + url + ' ya esta acortada '\
                                    + 'con ID = ' + str(fila.id))

        db = URLS(url=url)
        db.save()

    lista = URLS.objects.all()
    salida = 'Hay estas urls acortadas:' + '<br>'
    for fila in lista:
        salida += '<li>' + fila.url + ', ID = ' + str(fila.id)
    return HttpResponse(formulario + '<br>' + salida)

def Busqueda(request, recurso):
    try:
        db = URLS.objects.get(id=recurso)
        return HttpResponseRedirect(db.url)
    except URLS.DoesNotExist:
        return HttpResponse('Recurso /' + recurso + ' no disponible')
   
    
