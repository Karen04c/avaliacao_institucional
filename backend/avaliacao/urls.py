from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_avaliacoes, name="lista_avaliacoes"),
    path("pendentes/", views.avaliacoes_pendentes, name="avaliacoes_pendentes"),
]