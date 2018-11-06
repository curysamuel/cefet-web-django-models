from django.db import models

# Create your models here.


class EstiloMusical(models.Model):
	descrição = models.CharField(max_length=100)

	def __str__(self):
		return self.descrição


class Musico(models.Model):
	nome = models.CharField(max_length=1000)
	email = models.EmailField(max_length=200)
	idade = models.IntegerField()
	ativo = models.BooleanField()
    sexo = models.CharField(max_length=20)
    
	def __str__(self):
		return self.nome



class Banda(models.Model):
	nome = models.CharField(max_length=1000)
	email = models.EmailField(max_length=200)
	estilo = models.ForeignKey(EstiloMusical, on_delete=models.PROTECT)
	musicos = models.ManyToManyField(Musico, related_name='bandas')

	def __str__(self):
		return self.nome



