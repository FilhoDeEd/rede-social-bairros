from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from user_profile.models import Neighborhood, UserProfile


class Forum(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField(max_length=2047)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.PROTECT)
    owner = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

    # Campos de estatísticas (melhor fazer um cálculo complexo mas que não atulizar o tempo todo, somente de tempos em tempos)
        # Por hora, vamos só contar os inscritos
    subscribers_count = models.IntegerField(default=0)
    # posts_count = models.IntegerField(default=0) # Somente contar os comentários é falho (posso espamar em meu forum)
    # views_count = models.IntegerField(default=0) # Tem o mesmo problema do campo acima. É necessário um cálculo mais avançado

    # Controle de popularidade
    popularity = models.FloatField(default=0.0)  # Pode ser calculada no futuro

    # Controle de status (parece uma boa, mas n é necessário por agr) 
    #is_active = models.BooleanField(default=True) # Permitir ou não novos comentários
    #is_archived = models.BooleanField(default=False) # Remove o forum da visualização 

    # Campos de data
    creation_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField()

    # Sem banner por enquanto
    #banner = models.ImageField(upload_to='forum_banners/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation_date = timezone.now()

        self.update_date = timezone.now()

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Forum.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def add_subscriber(self):
        """Adiciona um inscrito ao fórum."""
        self.subscribers_count += 1

    def remove_subscriber(self):
        """Remove um inscrito do fórum."""
        if self.subscribers_count > 0:
            self.subscribers_count -= 1

    def calculate_popularity(self):
        """Calcula popularidade com base em métricas do fórum."""
        self.popularity = self.subscribers_count * 10

    def __str__(self):
        return self.title
