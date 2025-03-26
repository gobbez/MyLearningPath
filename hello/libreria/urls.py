from django.urls import path, re_path
from . import views
from . import views_wiki

urlpatterns = [
    path('', views.libri, name="libri"),
    re_path('^(\d+)/$', views.libro, name="libro"),
    re_path(r'^acquistati/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$', views.libri_per_data_acquisto),
    re_path('^autore/(?P<pk>\d+)/$', views.libri_autore, name='libri_autore'),
    re_path('^genere/(?P<pk>\d+)/$', views.libri_genere, name='libri_genere'),
    re_path('^ricerca/$', views_wiki.ricerca, name='libri_ricerca'),
]