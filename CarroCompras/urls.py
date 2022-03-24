from unicodedata import name
from django.urls import path
from . import views

app_name='carro' #namespace de esta forma para llamar a las funciones podemos poner 'carro/funcion requerida'

urlpatterns = [         
    path('agregar/<int:producto_id>/',views.agregar_producto,name='agregar'),
    path('restar/<int:producto_id>/',views.restar_producto,name='restar'),
    path('eliminar/<int:producto_id>/',views.eliminar_producto,name='eliminar'),
    path('limpiar/',views.limpiar_carro,name='limpiar'),
    
      ]
