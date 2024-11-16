from django.db import models



class User_profile(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cellphone = models.CharField(max_length=20)
    perfil_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  ## revisar a ideia de upload_to
    birthday = models.DateField(blank=True, null=True)
    trust_rate = models.FloatField()  # Definir isso melhor quando houver um cálculo para definir o que é isso
    active = models.BooleanField(default=True)

    #stutus  === entender o que é

    #FK id_user

    #Ver com deve ser feitos esses ultimos tópicos
    #neighborhood
    #state
    #locality
    #country

    def __str__(self):
        return self.name