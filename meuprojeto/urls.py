"""meuprojeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enquetes import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.bemvindo, name='home'),
=======
    path('', views.bemvindo),
>>>>>>> bc9653b3a3fe156877d4fddb95dc093131ad7590
    path('add_assunto/', views.add_assunto, name='add_assunto'),
    path('list_assuntos', views.list_assuntos, name='list_assuntos'),
    path('add_perfil/', views.add_perfil, name='add_perfil'),
    path('list_perfis', views.list_perfis, name='list_perfis'),
    path('add_postagem/', views.add_postagem, name='add_postagem'),
    path('list_postagens', views.list_postagens, name='list_postagens'),
    path('add_curso/', views.add_curso, name='add_curso'),
    path('list_cursos', views.list_cursos, name='list_cursos'),
    path('add_disciplina/', views.add_disciplina, name='add_disciplina'),
    path('list_disciplinas', views.list_disciplinas, name='list_disciplinas'),
]
