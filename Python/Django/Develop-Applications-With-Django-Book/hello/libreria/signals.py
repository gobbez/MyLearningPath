from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import Signal

from .helpers import log_colorato
from .models import Autore

@receiver(post_save, sender=Autore)
def libro_post_save(sender, instance, created, **kwargs):
    if created:
        log_colorato(f"Un nuovo {sender.__name__} è stato creato: {instance}")
    else:
        log_colorato(f"Un {sender.__name__} esistente è stato aggiornato: {instance}")


utenti_connessi = Signal()
elenco_utenti = set()

@receiver(utenti_connessi)
def utenti_connessi_handler(sender, connesso, **kwargs):
    if connesso:
        elenco_utenti.add(sender.username)
    else:
        if sender.username in elenco_utenti:
            elenco_utenti.remove(sender.username)
    log_colorato(f"Utenti connessi: {','.join(elenco_utenti)}")


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    utenti_connessi.send(user, connesso=True)


@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    utenti_connessi.send(user, connesso=False)
