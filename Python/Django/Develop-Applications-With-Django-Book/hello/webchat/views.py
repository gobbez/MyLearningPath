from django.shortcuts import render, redirect
from django.urls import reverse

def webchat(request, *arg, **kwargs):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.path}")
    context = {}
    return render(request, "webchat/webchat.html", context)
