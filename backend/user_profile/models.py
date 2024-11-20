from django.db import models


class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    locality = models.CharField(max_length=2)
    country = models.CharField(max_length=255, default='Brasil')

    def __str__(self):
        return f"{self.name}, {self.locality}, {self.state}"


class User_profile(models.Model):

    STATUS_CHOICES = [
        # ('active', 'Active'),
        # ('inactive', 'Inactive'),
        # ('banned', 'Banned'),
    ]

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cellphone = models.CharField(max_length=20)
    #perfil_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    trust_rate = models.FloatField()
    active = models.BooleanField(default=True)
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.SET_NULL,  # Define o comportamento ao excluir o bairro
        null=True,
        blank=True,
        related_name="residents",  # Permite acessar os usuários pelo bairro

    status = models.CharField(
            max_length=10, 
            choices=STATUS_CHOICES, 
            default='active'
        )

        #FK id_account

    )

    def __str__(self):
        return f"{self.name} {self.surname}"
