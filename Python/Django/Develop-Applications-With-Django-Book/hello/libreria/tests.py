from django.test import TestCase
from .models import Autore

class AutoreTest(TestCase):
    def test_(self):
        Autore.objects.create(nome="John", cognome="Cleese")
        self.assertEqual(len(Autore.objects.all()), 1)
        self.assertEqual(Autore.objects.get(cognome="Cleese").nome, 'John')

