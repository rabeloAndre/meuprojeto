from django.db import models

class Assunto(models.Model):
    nome = models.CharField(max_length=255)
    materia = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
	nome_usuario = models.CharField(max_length=100)

	def __str__(self):
		return self.nome_usuario

class Postagem(models.Model):
   	texto = models.CharField(max_length=255)
   	perfil = models.ForeignKey('Perfil',
		related_name = 'postagem',
		on_delete=models.CASCADE)

   	def __str__(self):
   		return self.texto

class Curso(models.Model):
	nome = models.CharField(max_length=100)
	carga_horaria = models.IntegerField()
	area = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Disciplina(models.Model):
   	nome = models.CharField(max_length=100)
   	carga_horaria = models.IntegerField()
   	curso = models.ManyToManyField(Curso)

   	def __str__(self):
   		return self.nome

   	curso = models.ManyToManyField(Curso,
   		related_name = 'curso')

   	def __str__(self):
   		return self.texto
