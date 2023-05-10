from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note




def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        new_note = Note(title= title , content= content)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all().order_by('-created_at')
        return render(request, 'notes/index.html', {'notes': all_notes})


def creditos(request):
    return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por Esther Caroline</p>")

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})