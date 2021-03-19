from django.shortcuts import render
from visitantes.forms import VisitanteForm


def registrar_visitante(request):

    context = {
        "nome_pagina" : "Registrar visitante",
        "form" : VisitanteForm(),

    }

    return render(request,"registrar_visitante.html", context)