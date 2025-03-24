from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def libri(request):
    elenco = ""
    for libro in Libro.objects.all().order_by('titolo'):
        elenco += (f'"{libro.titolo}" di {libro.autore}, {libro.genere}<br>')
    return HttpResponse(elenco)

def libro(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
        return HttpResponse(f'"{libro.titolo}" di {libro.autore}, {libro.genere}<br>')
    except:
        return HttpResponse(f"Codice {pk} inesistente")

def libri_per_data_acquisto(request, mese, anno):
    libri = Libro.objects.filter(data_acquisto__year=int(anno), data_acquisto__month=int(mese)).order_by('titolo')
    elenco = ""
    for libro in libri:
        elenco += (f'"{libro.titolo}" acquistato il: {libro.data_acquisto}<br>')
    if elenco == "":
        elenco = "Nessun libro"
    return HttpResponse(elenco)