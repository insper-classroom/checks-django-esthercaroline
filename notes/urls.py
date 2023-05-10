from django.urls import path
from . import views

urlpatterns = [
    path('creditos/', views.creditos, name='creditos'),
    path('anotacoes/<int:note_id>/editar', views.edit_note, name='edit-note'),
    path('anotacoes/<int:note_id>/apagar', views.delete_note, name='delete-note'),
    path('', views.index, name='index')
]