from django.db import models
from django.contrib.auth.models import User #primeiro app utilizado
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length= 255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # faz com que o post seja deletado caso o usuario que é foreign key seja deletado
    body = models.TextField() #corpo do texto livre em tamanho
    created = models.DateTimeField(auto_now_add=True) #cria automaticamente a data do post 
    updated = models.DateTimeField(auto_now=True) #coloca a data da ultima atualizacao do post

    class Meta:
         ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

