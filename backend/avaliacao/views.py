from django.http import JsonResponse
from .models import Avaliacao


def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values()
    return JsonResponse(list(avaliacoes), safe=False)


def avaliacoes_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status="PENDENTE").values()
    return JsonResponse(list(avaliacoes), safe=False)