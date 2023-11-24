from django.db import models
from datetime import date


class Livros(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=date.today) 
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, blank=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolução = models.DateTimeField(blank=True, null=True)
    tempo_emprestimo = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.nome

