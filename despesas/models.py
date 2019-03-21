from django.conf import settings
from django.db import models
from django.utils import timezone


class Despesas(models.Model):

    CATEGORIA_CHOICES = (
        (1, "Alimentação"),
        (2, "Cuidados pessoais"),
        (3, "Transporte/Combustível/Estacionamento"),
        (4, "Água/Luz/Telefone"),
        (5, "Outros"),
        (6, "Passeios/Viagens"),
        (7, "Cinema/Teatro"),
        (8, "Farmacia"),
        (9, "Vestuário"),
        (10, "Cuidados com animais de estimação"),

    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    descricao = models.TextField(max_length=50)
    created_date = models.DateField(verbose_name='Data da compra')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.BooleanField(default=False, verbose_name='')
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES, default=1)

    def __str__(self):
        return self.descricao

    def total(self, despesas):
        soma = 0
        for i in despesas:
            soma += i.valor
        return soma

    def total_dinheiro(self, despesas):
        soma = 0
        for i in despesas:
            if (i.tipo == False):
                soma += i.valor
        return soma

    def total_cartao(self, despesas):
        soma = 0
        for i in despesas:
            if (i.tipo == True):
                soma += i.valor
        return soma
