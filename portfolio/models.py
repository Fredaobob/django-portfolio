from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    technology = models.CharField(max_length=20, verbose_name="Tecnologia")
    image = models.ImageField(upload_to='images/', verbose_name="Imagem")
    link = models.URLField(blank=True, verbose_name="Link do Projeto")

    def __str__(self):
        return self.title
