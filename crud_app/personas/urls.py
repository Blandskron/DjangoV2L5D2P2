# personas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_persona, name='crear_persona'),
    path('listar/', views.listar_personas, name='listar_personas'),
    path('filtrar/', views.filtrar_personas, name='filtrar_personas'),
    path('excluir/', views.excluir_personas, name='excluir_personas'),
    path('ordenar/', views.ordenar_personas, name='ordenar_personas'),
    path('actualizar/<int:id>/', views.actualizar_persona, name='actualizar_persona'),
    path('eliminar/<int:id>/', views.eliminar_persona, name='eliminar_persona'),
]