from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from .models import *

def libri(request):
    context = {'libri': Libro.objects.all().order_by('titolo')}
    return render(request, "libri.html", context)

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

def libri_genere(request, pk):
    genere = get_object_or_404(Genere, pk=pk)
    context = {'libri': Libro.objects.filter(genere=genere).order_by('titolo'), 'genere': genere}
    return render(request, "libri.html", context)

def libri_autore(request, pk):
    autore = get_object_or_404(Autore, pk=pk)
    context = {'libri': Libro.objects.filter(autore=autore).order_by('titolo'), 'autore': autore}
    return render(request, "libri.html", context)


def cerca(request):
    return render(request, "libreria/cerca.html")

def risultati(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Controllo richiesta AJAX
        valore = request.GET.get('cerca', '').strip()
        if valore:
            risultati = Libro.objects.select_related("autore", "genere").filter(
                Q(titolo__icontains=valore) |
                Q(autore__cognome__icontains=valore) |
                Q(autore__nome__icontains=valore)
            )
        else:
            risultati = Libro.objects.none()

        html = render_to_string('libreria/risultati.html', {'libri': risultati}, request=request)  # Aggiunto request=request

        return JsonResponse({'html': html})  # Restituisce JSON valido

    return JsonResponse({'error': 'Richiesta non valida'}, status=400)