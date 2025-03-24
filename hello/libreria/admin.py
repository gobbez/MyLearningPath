from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro)