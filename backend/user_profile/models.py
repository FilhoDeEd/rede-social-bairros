from django.db import models
from accounts import models

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

    def __str__(self):
        return f"{self.name}, {self.locality}, {self.state}"


class User_profile(models.Model):

    #checar todos os status possíveis e ver se algum garante "vantagens"

    STATUS_CHOICES = [
        # ('active', 'Active'),
        # ('inactive', 'Inactive'),
        # ('banned', 'Banned'),
    ]

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cellphone = models.CharField(max_length=20)

    trust_rate = models.FloatField()
    active = models.BooleanField(default=True)
    neighborhood = models.ForeignKey(Neighborhood,)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    #parte comentada para analise posterior
    #id_account = models.ForeignKey(accounts)
    #perfil_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
