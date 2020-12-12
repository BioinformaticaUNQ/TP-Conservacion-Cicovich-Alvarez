from typing import Any
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from Bio.Application import ApplicationError
from .core.fasta import getSequence
from .core.clustal import getAlignment_flat
from .core.conservation import getConservedZone_json
from .core.dssp import calculateSecondaryStructureConservation_json

def fasta(request, **kwargs: Any):
    return JsonResponse({'sequence': getSequence(kwargs['pID'])})

def clustal(request, **kwargs: Any):
    try:
        return JsonResponse({'alignment': getAlignment_flat(kwargs['pID'], float(kwargs['filterEValue']))})
    except ApplicationError as e:
        return HttpResponse(status = 404, content= JsonResponse({'message': e.args[3]}))
    except:
        return HttpResponseServerError(JsonResponse({'message': 'Error procesando las secuencias a alinear.'}))

def conservation(request, **kwargs: Any):
    try:
        return JsonResponse({'conservation': getConservedZone_json(kwargs['pID'], float(kwargs['filterEValue']), kwargs['filterConservationPersentage'])})
    except Exception as e:
        if hasattr(e, 'message'):
            message = e.message
        elif hasattr(e, 'reason'):
            message = e.reason
        else:
            message = e.args[1]
        return HttpResponse(status = 404, content= JsonResponse({'message': message}))
    except:
        return HttpResponseServerError(JsonResponse({'message': 'Error calculando la conservacion.'}))

def conservation2(request, **kwargs:Any):
    try:
        return JsonResponse({'conservation': calculateSecondaryStructureConservation_json(kwargs['pID'], float(kwargs['filterEValue']), kwargs['filterConservationPersentage'])})
    except Exception as e:
        if hasattr(e, 'message'):
            message = e.message
        elif hasattr(e, 'reason'):
            message = e.reason
        else:
            message = e.args[1]
        return HttpResponse(status = 404, content= JsonResponse({'message': message}))
    except:
        return HttpResponseServerError(JsonResponse({'message': 'Error calculando la conservacion.'}))
