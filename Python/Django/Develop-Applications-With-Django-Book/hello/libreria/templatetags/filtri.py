from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
register = template.Library()

@register.filter
def bibliografico(autore):
    return mark_safe(
        f"<strong>{conditional_escape(autore.cognome)}</strong>, "
        f"{conditional_escape(autore.nome)}"
    )

