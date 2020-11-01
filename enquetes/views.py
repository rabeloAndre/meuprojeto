from django.shortcuts import render, redirect
from enquetes.models import *
from enquetes.forms import *

def bemvindo(request):
	return render(request,'bemvindo.html')


def list_assuntos(request):
    assuntos = Assunto.objects.all()
    return render(request, "list_assuntos.html", {'assuntos': assuntos})

def add_assunto(request):
    if request.method == "POST":
        form = AssuntoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_assuntos')
    else:
        form = AssuntoForm()
        return render(request, "add.html", {'form': form})


def list_perfis(request):
    perfis = Perfil.objects.all()
    return render(request, "list_perfis.html", {'perfis': perfis})

def add_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_perfis')
    else:
        form = PerfilForm()
        return render(request, "add.html", {'form': form})


def list_postagens(request):
    postagens = Postagem.objects.all()
    return render(request, "list_postagens.html", {'postagens': postagens})

def add_postagem(request):
    if request.method == "POST":
        form = PostagemForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_postagens')
    else:
        form = PostagemForm()
        return render(request, "add.html", {'form': form})


def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "list_cursos.html", {'cursos': cursos})

def add_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_cursos')
    else:
        form = CursoForm()
        return render(request, "add.html", {'form': form})


def list_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, "list_disciplinas.html", {'disciplinas': disciplinas})

def add_disciplina(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            form.save_m2m()
            return redirect('list_disciplinas')
    else:
        form = DisciplinaForm()
        return render(request, "add.html", {'form': form})