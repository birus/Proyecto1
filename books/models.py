from django.db import models

# Create your models here.
class Editor(models.Model):
	name=models.CharField('Nombre', max_length=30)
	address=models.CharField('Direccion', max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()

	def __str__(self):
		return self.name

#Para que siempre se ordene por el Nombre	
	class meta:
		ordering=["name"]

#class Admin:
#		pass

		

class Autor(models.Model):
	salutatio=models.CharField(max_length=10, verbose_name='Saludo')
	first_name=models.CharField(max_length=30, verbose_name='Nombre')
	last_name=models.CharField(max_length=40, verbose_name='Apellido')
	email=models.EmailField(blank=True, verbose_name='e-mail')
	headshot=models.ImageField(upload_to='/temp',blank=True, verbose_name='Foto')

	def __str__(self):
		return '%s%s'%(self.first_name, self.last_name)

#	class Admin:
#		pass

class Book(models.Model):
	title=models.CharField(max_length=100)
	autores=models.ManyToManyField(Autor)
	editor=models.ForeignKey(Editor)
	publicatio_date=models.DateField()

	def __str__(self):
		return self.title
#	class Admin:
#		pass