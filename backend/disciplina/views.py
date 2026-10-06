from django.http import JsonResponse
from .models import Disciplina


def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all().values()
    return JsonResponse(list(disciplinas), safe=False)