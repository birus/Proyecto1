from django.db import models

# Create your models here.
class Editor(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()

	def __str__(self):
		return self.name

#Para que siempre se ordene por el Nombre	
	class meta:
		ordering=["name"]

		

class Autor(models.Model):
	salutatio=models.CharField(max_length=10)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()
	headshot=models.ImageField(upload_to='/temp')

	def __str__(self):
		return '%s%s'%(self.first_name, self.last_name)

class Book(models.Model):
	title=models.CharField(max_length=100)
	autores=models.ManyToManyField(Autor)
	editor=models.ForeignKey(Editor)
	publicatio_date=models.DateField()

	def __str__(self):
		return self.title
