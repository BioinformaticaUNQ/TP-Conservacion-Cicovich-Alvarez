from typing import Any
from django.http import JsonResponse
from .core.fasta import getSequence
from .core.clustal import getAlignment_flat
from .core.conservation import getConservedZone_json
from .core.dssp import calculateSecondaryStructureConservation_json

def fasta(request, **kwargs: Any):
    return JsonResponse({'sequence': getSequence(kwargs['pID'])})

def clustal(request, **kwargs: Any):
    return JsonResponse({'alignment': getAlignment_flat(kwargs['pID'], float(kwargs['filterEValue']))})

def conservation(request, **kwargs: Any):
    return JsonResponse({'conservation': getConservedZone_json(kwargs['pID'], float(kwargs['filterEValue']), kwargs['filterConservationPersentage'])})

def conservation2(request, **kwargs:Any):
    return JsonResponse({'conservation': calculateSecondaryStructureConservation_json(kwargs['pID'], float(kwargs['filterEValue']), kwargs['filterConservationPersentage'])})
