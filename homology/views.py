from typing import Any
from django.shortcuts import render
from django.http import HttpResponse

from .models import Homology

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
    )

def homologyDetailView(request, **kwargs: Any):
    try:
        context = {
            'homology': Homology(kwargs['pID'], kwargs['filterEValue'], kwargs['filterConservationPersentage1'], kwargs['filterConservationPersentage2']),
        }
        return render(
            request, 
            'homology/homology_detail.html', 
            context
        )
    except:
        return HttpResponse("<h2 style=\"text-align: center;\">El PDB Id (" + kwargs['pID'] + ") ingresado no pudo ser encontrado.</h2>")