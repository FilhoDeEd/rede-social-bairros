from django.db import models
from account.models import Account


class UfChoices(models.TextChoices):
    AC = 'AC', 'Acre'
    AL = 'AL', 'Alagoas'
    AP = 'AP', 'Amapá'
    AM = 'AM', 'Amazonas'
    BA = 'BA', 'Bahia'
    CE = 'CE', 'Ceará'
    DF = 'DF', 'Distrito Federal'
    ES = 'ES', 'Espírito Santo'
    GO = 'GO', 'Goiás'
    MA = 'MA', 'Maranhão'
    MT = 'MT', 'Mato Grosso'
    MS = 'MS', 'Mato Grosso do Sul'
    MG = 'MG', 'Minas Gerais'
    PA = 'PA', 'Pará'
    PB = 'PB', 'Paraíba'
    PR = 'PR', 'Paraná'
    PE = 'PE', 'Pernambuco'
    PI = 'PI', 'Piauí'
    RJ = 'RJ', 'Rio de Janeiro'
    RN = 'RN', 'Rio Grande do Norte'
    RS = 'RS', 'Rio Grande do Sul'
    RO = 'RO', 'Rondônia'
    RR = 'RR', 'Roraima'
    SC = 'SC', 'Santa Catarina'
    SP = 'SP', 'São Paulo'
    SE = 'SE', 'Sergipe'
    TO = 'TO', 'Tocantins'


class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=UfChoices.choices)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default='Brazil')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'state', 'locality', 'country'],
                name='unique_neighborhood'
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.locality}, {self.state}'


class UserProfile(models.Model):

    #checar todos os status possíveis e ver se algum garante "vantagens"

    STATUS_CHOICES = [
        # ('active', 'Active'),
        # ('inactive', 'Inactive'),
        # ('banned', 'Banned'),
    ]


    trust_rate = models.FloatField()
    active = models.BooleanField(default=True)
    neighborhood = models.ForeignKey(Neighborhood,)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    id_account = models.ForeignKey(Account)

    #parte comentada para analise posterior
    
    #perfil_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
