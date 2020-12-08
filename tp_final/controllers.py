
from django.http import JsonResponse
from .core.fastaCreator import getFasta
def prueba(request):
    return JsonResponse({'sequence': getFasta('1LXA')})