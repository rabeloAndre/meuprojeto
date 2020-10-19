from django.forms import ModelForm
from enquetes.models import *
from django import forms

class AssuntoForm(ModelForm):
	class Meta:
		model = Assunto
		fields = '__all__'

class PerfilForm(ModelForm):
	class Meta:
		model = Perfil
		fields = ['nome_usuario']

class PostagemForm(ModelForm):
	class Meta:
		model = Postagem
		fields = '__all__'

class CursoForm(ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'

class DisciplinaForm(ModelForm):
	class Meta:
		model = Disciplina
		fields = '__all__'