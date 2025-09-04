from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'({self.id}) {self.nome} | {self.estoque} | R$ {self.preco}'
