from django.db import models
from django.contrib.auth.models import User #importa el modelo autor para establecer una relacion entre un usuario y el post que haga en el blog

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) # el auto es para que cuando se cree se cargue sola la fecha
    updated=models.DateTimeField(auto_now_add=True)
    #Clase Interna
    class Meta: #la clase Meta dentro de los modelos especifica lo que son los datos Meta de nuestras clases
        verbose_name='categoria' #sirve para especificar el nombre del modelo dentro de la base de datos como los campos
        verbose_name_plural='categorias'

    def __str__(self): #para que nos devuelva el nombre del servicio
        return self.nombre
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True,blank=True) # se guardaran en la carpeta servicios dentro de la carpeta blog null y blank para que pueda ser opcional la imagen
    autor=models.ForeignKey(User,on_delete=models.CASCADE) # Cascade sirve para si el usuario se borra que se borren todos sus post
    categorias=models.ManyToManyField(Categoria)#relacion many to many entre post y categorias ya que un post puede estar en varias categorias y una categoria en varios post
    created=models.DateTimeField(auto_now_add=True) # el auto es para que cuando se cree se cargue sola la fecha
    updated=models.DateTimeField(auto_now_add=True)

    #Clase Interna
    class Meta: #la clase Meta dentro de los modelos especifica lo que son los datos Meta de nuestras clases
        verbose_name='post' #sirve para especificar el nombre del modelo dentro de la base de datos como los campos
        verbose_name_plural='posts'

    def __str__(self): #para que nos devuelva el nombre del servicio
        return self.titulo