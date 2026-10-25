from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from django.shortcuts import render

# Create your views here.
def listar_livros(request):
    livros_salvos = Livro.objects.all()
    return render(request, 'listar.html', {'livros': livros_salvos})

def criar_livro(request):
    if request.method == 'POST':
        v_titulo = request.POST.get('titulo')
        v_autor = request.POST.get('autor')
        
        Livro.objects.create(titulo=v_titulo, autor=v_autor)
        
        return redirect('listar')
    return render(request, 'form.html')

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    
    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.save()
        return redirect('listar')
    
    return render(request, 'form.html', {'livro': livro})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('listar')