from django.http import JsonResponse
from .models import Aluno


def lista_alunos(request):
    alunos = Aluno.objects.all().values()
    return JsonResponse(list(alunos), safe=False)