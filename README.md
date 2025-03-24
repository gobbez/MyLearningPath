# DjangoBook
Python Django excercises of the book "Sviluppare applicazioni con Django (M. Beri)"

![alt text](book.jpg "Sviluppare applicazioni con Django")

### Details
This repository is used to study from the above mentioned book. <br>
I'll add the steps explained with a description. 
The book will start from the very basics to an advanced level.

Feel free to clone this repo!

## Step-By-Step Learning

### Chapter 1. Install Django + "Hello World"
<li>First thing to do is install Django (in a virtual environment):</li>

```bash
pip install django
```
<li>Create the new Django project with this command:</li>

```bash
django-admin startproject hello
```

<li>Set the SECRET_KEY (in hello/settings.py) in another file and add it in .gitignore</li>
<li>Create a new View in hello/views.py with a "Hello World" message.</li>
<li>Create the new route calling the View in hello/urls.py.</li>
<li>Run the server to see the new route with the "Hello World" message.</li>

```bash
cd hello
python manage.py runserver
(go to http://127.0.0.1:8000/hello/)
```

<br>

### Chapter 2. Database, ORM, Model
<li>Create a new application with the command:</li>

```bash
django-admin startapp libreria
```

<li>Add the new application in INSTALLED_APPS in hello/settings.py</li>
<li>Create a new model: libreria/models.py with 3 new table (Autore, Genere, Libro)</li>
<li>Create migrations for the new tables</li>

```bash
python manage.py makemigrations
python manage.py migrate
```
<br>

### Chapter 3. Admin
<li>Modify file libreria/admin.py like this:</li>

```bash
from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro)
```
<li>Create a superuser from command and following instructions (to set username, email, password)</li>

```bash
python manage.py createsuperuser
```
<li>Start server and go to http://127.0.0.1:8000/admin/</li>
<li>(optional) In each table (libreria/models.py) add a class Meta to make the visualizzation of the table names correct:</li>

```bash
class Meta:
    verbose_name_plural = "Autori" (# same thing for "Generi" and "Libri")
```

<li>In each table (libreria/models.py) ad a __str__(self): function that returns correctly the column names</li>

```bash
class __str__(self):
    return f"{self.nome} {self.cognome}"  (# same thing for other tables)
```

<li>Create a new libro, new autore and new genere via admin panel on the browser</li>
Now you are free to add/modify/delete as many rows in the tables as you want!

<br>

### Chapter 4. Url

<li>Add a new route 'libri', in the hello/urls.py, importing the libreria/views.py and its class (libri)</li>
<li>Modify libreria/views.py to create the class libri: this class will show the list of books (for now without using Templates)</li>
<li>Start the server and go to http://127.0.0.1:8000/libri/ to see all the books you have added</li>
<li>Create a new route in hello/urls.py to use a re_path to check what book the user is searching:</li>

```bash
from django.contrib import admin
from django.urls import path, re_path

from hello import views
from libreria import views as views_libreria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('libri/', views_libreria.libri, name="libri"),
    re_path('^libri/(\d+)/$', views_libreria.libro, name="libro"),
]
```

<li>Create corresponding functions in libreria/views.py (for now without using Templates): </li>

```bash
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
```

<li>Modify libreria/models.py to add a DateField in the table (class) Libro</li>
<li>Execute makemigrations and migrate on command line</li>
<li>Modify libreria/admin.py to create a better visualization of the books:</li>

```bash
from django.contrib import admin

# Register your models here.
from . import models

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'autore', 'genere', 'data_acquisto']

admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro, LibroAdmin)
```

<li>Start server and go to http://127.0.0.1:8000/admin/libreria/libro/ to see the new html table of your books</li>
<li>In hello/urls.py to create a new route to search for data too:</li>

```bash
re_path(r'^libri/acquistati/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$', views_libreria.libri_per_data_acquisto),
```
<li>In libreria/views.py add the new function for that route:</li>

```bash
def libri_per_data_acquisto(request, mese, anno):
    libri = Libro.objects.filter(data_acquisto__year=int(anno), data_acquisto__month=int(mese)).order_by('titolo')
    elenco = ""
    for libro in libri:
        elenco += (f'"{libro.titolo}" acquistato il: {libro.data_acquisto}<br>')
    if elenco == "":
        elenco = "Nessun libro"
    return HttpResponse(elenco)
```

<li>Start server, add a date in a book in the admin panel, then try to filter for data (example below)</li>

```bash
http://127.0.0.1:8000/libri/acquistati/2025/3/
```

Now you can filter for data as well!