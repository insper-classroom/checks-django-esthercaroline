from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note




def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        print(f'Titulo={title}\nConteudo={content}\n')
        new_note = Note(title= title , content= content)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all().order_by('-created_at')
        return render(request, 'notes/index.html', {'notes': all_notes})


def creditos(request):
    return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por Esther Caroline</p>")