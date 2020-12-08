from typing import Any
from django.shortcuts import render

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
    context = {
        'homology': Homology(kwargs['pk']),
    }
    return render(
        request, 
        'homology/homology_detail.html', 
        context
    )