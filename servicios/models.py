from django.db import models

# Create your models here.
class Servicio(models.Model): #siempre debe heredar models.Model
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios') # las imagenes cargadas para este modelo se guardaran en la carpeta servicios dentro de la carpeta media
    created=models.DateTimeField(auto_now_add=True) # el auto es para que cuando se cree se cargue sola la fecha
    updated=models.DateTimeField(auto_now_add=True)
    #Clase Interna
    class Meta: #la clase Meta dentro de los modelos especifica lo que son los datos Meta de nuestras clases
        verbose_name='servicio' #sirve para especificar el nombre del modelo dentro de la base de datos como los campos
        verbose_name_plural='servicios'

    def __str__(self): #para que nos devuelva el nombre del servicio
        return self.titulo