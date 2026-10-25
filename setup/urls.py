from django.contrib import admin
from django.urls import path
from livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_livros, name='listar'),
    path('novo/', views.criar_livro, name='criar'),
    path('editar/<int:id>/', views.editar_livro, name='editar'),
    path('deletar/<int:id>/', views.deletar_livro, name='deletar'),
]
