from django.shortcuts import render
from visitantes.models import Visitante


def index(request):
    
    context = {    
        "todos_visitantes" : Visitante.objects.all(),
    }

    return render(request, "index.html",context )

