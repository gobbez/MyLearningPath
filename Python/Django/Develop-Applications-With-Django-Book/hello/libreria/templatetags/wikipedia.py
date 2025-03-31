import json
from urllib import parse
from urllib.request import urlopen
from django import template
from django.core.cache import cache

register = template.Library()

# URL for Wikipedia search
wiki_link = "https://it.wikipedia.org/wiki/"
wiki_url_api = "http://it.wikipedia.org/w/api.php?action=query&format=json&srlimit=3&list=search&srsearch={}"

class Pagina:
    def __init__(self, title):
        self.title = title
        self.url = f"http://it.wikipedia.org/wiki/{self.title}"

class GetWikipediaList(template.Node):
    def __init__(self, book, varname):
        self.book = book
        self.varname = varname

    def render(self, context):
        book = self.book.resolve(context)
        url = wiki_url_api.format(parse.quote(book.titolo))

        # Use cache for faster results
        risultati = cache.get(url)
        if not risultati:
            dati = urlopen(url)
            valori = json.load(dati)
            risultati = [Pagina(valore['title']) for valore in valori['query']['search']]
            cache.set(url, risultati, 60*60)
        context[self.varname] = risultati
        return ''

@register.tag
def get_wikipedia_info(parser, token):
    tokens = token.contents.split()
    if len(tokens) != 5:
        raise template.TemplateSyntaxError(f"Il tag {tokens[0]} richiede 5 argomenti")
    if tokens[1] != "for":
        raise template.TemplateSyntaxError("Il primo argomento deve essere 'for'")
    if tokens[3] != 'as':
        raise template.TemplateSyntaxError("Il terzo argomento deve essere 'as'")
    return GetWikipediaList(book=template.Variable(tokens[2]), varname=tokens[4])

