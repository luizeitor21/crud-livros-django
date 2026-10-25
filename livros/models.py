from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)

def __str__(self):
        return f"{self.titulo} - {self.autor}"