
from typing import Any
from django.http import JsonResponse
from .core.fasta import getSequence
def fasta(request, **kwargs: Any):
    return JsonResponse({'sequence': getSequence(kwargs['pk'])})