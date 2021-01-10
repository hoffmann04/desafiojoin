from django.urls import path
from . import views

app_name = 'alvos'
urlpatterns = [
    #views
    path('adicionar/', views.adicionar_alvo, name='adicionar_alvo'),
    path('editar/<int:alvo_id>/', views.edit_alvos, name='edit_alvos'),
    path('deletar/<int:alvo_id>/', views.deletar_alvo, name='deletar_alvo'),
    path('', views.index, name='index'),
]