import json
from urllib import parse
from urllib.request import urlopen
from django import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

class WikisearchForm(forms.Form):
    autore = forms.IntegerField(widget=forms.Select(
        choices=[(autore.pk, autore) for autore in Autore.objects.all()]))
    wikipedia = forms.CharField(widget=forms.Select(
        choices=(("it", "Italiana"), ("en", "Inglese"))))
    limite = forms.IntegerField(initial=10,
                                widget=forms.RadioSelect(
                                    choices=((10, "10"), (50, "50"), (100, "100"))))

    def clean_limite(self):
        if (self.cleaned_data['limite'] > 50 and self.cleaned_data['wikipedia'] == 'en'):
            raise forms.ValidationError("Massimo 50 risultati in inglese")
        return self.cleaned_data['limite']


@login_required
def ricerca(request):
    wiki_url_api = ("https://{wikipedia}.wikipedia.org/w"
                    "/api.php?action=query&format=json"
                    "&srlimit={limite}&list=search&srsearch={autore}")
    wiki_link = "https://{wikipedia}.wikipedia.org/wiki/"
    context = {}
    if request.method == "POST":
        form = WikisearchForm(request.POST)
        if form.is_valid():
            autore = get_object_or_404(Autore, pk=form.cleaned_data['autore'])
            url = wiki_url_api.format(wikipedia=parse.quote(form.cleaned_data['wikipedia']),
                                      limite=form.cleaned_data['limite'],
                                      autore=parse.quote(autore.cognome))
            dati = urlopen(url)
            valori = json.loads(dati.read())
            context.update(link=wiki_link.format(wikipedia=form.cleaned_data['wikipedia']),
                           risultati=valori['query']['search'],)
    else:
        form = WikisearchForm()
    context.update(form=form)
    return render(request, 'libreria/wikisearch.html', context)