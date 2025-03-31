from django.contrib import admin

# Register your models here.
from . import models

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'autore', 'genere', 'data_acquisto']

admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro, LibroAdmin)
