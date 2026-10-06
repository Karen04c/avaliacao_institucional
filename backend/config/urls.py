from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/alunos/", include("aluno.urls")),
    path("api/disciplinas/", include("disciplina.urls")),
    path("api/avaliacoes/", include("avaliacao.urls")),
]