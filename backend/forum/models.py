from django.db import models
from django.utils import timezone

# Popular isso com uma base de dados
class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)

class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.PROTECT)
    # owner = # chave estrangeria para quem criou o fórum
    subscribers_count = models.IntegerField(default=1) # O dono deve ser inscrito no próprio fórum?
    popularity = models.FloatField() # Definir isso melhor quando houver um cálculo para definir o que é isso
    creation_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation_date = timezone.now()
        self.update_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
