from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import *
from .helpers import log_colorato


def aggiungi_storia(request, context={}, libro=None):
    libri_visitati = request.session.get('libri_visitati', {})
    if libro and str(libro.pk) not in libri_visitati:
        libri_visitati[str(libro.pk)] = libro.titolo

    request.session['libri_visitati'] = libri_visitati
    context.update(libri_visitati=libri_visitati)
    return context


def libri(request):
    log_colorato("COOKIE: \n")
    for cookie, valore in request.COOKIES.items():
        log_colorato(f"{cookie}: {valore}\n")

    libri_qs = Libro.objects.all().order_by('titolo')

    # Aggiungere paginazione
    paginator = Paginator(libri_qs, 2)  # 2 libri per pagina
    page = request.GET.get('page')
    libri = paginator.get_page(page)

    context = {'libri': libri}
    context = aggiungi_storia(request, context=context)
    return render(request, "libri.html", context)

def libro(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
        context = aggiungi_storia(request, context={'libro': libro}, libro=libro)
        return render(request, "libreria/libro.html", context)
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
    context = aggiungi_storia(request, context=context)
    return render(request, "libri.html", context)

def libri_autore(request, pk):
    autore = get_object_or_404(Autore, pk=pk)
    context = {'libri': Libro.objects.filter(autore=autore).order_by('titolo'), 'autore': autore}
    context = aggiungi_storia(request, context=context)
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

class LibriListView(ListView):
    model = Libro
    template_name = "libreria/libri.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return aggiungi_storia(self.request, context=context)


def cerca_htmx(request):
    return render(request, 'libreria/cerca_htmx.html')

def risultati_htmx(request):
    query = request.GET.get('q', '')
    if query:
        risultati = Libro.objects.filter(
            Q(titolo__icontains=query) |
            Q(titolo__icontains=query) |
            Q(autore__cognome__icontains=query) |
            Q(autore__nome__icontains=query)
        )
    else:
        risultati = []
    return render(request, 'libreria/risultati.html', {'libri': risultati})