from django.db import models

# Create your models here.

class Autore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    def __str__(self):
       return f"{self.nome} {self.cognome}"
    class Meta:
        verbose_name_plural = "Autori"

class Genere(models.Model):
    descrizione = models.CharField(max_length=30)
    def __str__(self):
       return f"{self.descrizione}"
    class Meta:
        verbose_name_plural = "Generi"

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.ForeignKey(Autore, on_delete=models.PROTECT)
    genere = models.ForeignKey(Genere, on_delete=models.PROTECT)
    data_acquisto = models.DateField(null=True, verbose_name="Data di acquisto")

    def __str__(self):
       return f"{self.titolo}"
    class Meta:
        verbose_name_plural = "Libri"