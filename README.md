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