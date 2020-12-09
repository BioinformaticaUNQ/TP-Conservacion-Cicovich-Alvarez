from typing import Any
from django.http import JsonResponse
from .core.fasta import getSequence
from .core.clustal import getAlignment_flat

def fasta(request, **kwargs: Any):
    return JsonResponse({'sequence': getSequence(kwargs['pk'])})

def clustal(request, **kwargs: Any):
    return JsonResponse({'alignment': getAlignment_flat(kwargs['pk'], 0.0000000000001)})