from django.urls import path
from . import views #el punto indica de donde se importa el views es dentro de la raiz
from django.conf import settings #agrego el settings para llamar 
from django.conf.urls.static import static #agrego los archivos static

urlpatterns = [
    
  
    path('',views.servicios,name='Servicios'), #como ya estamos dentro de la carpeta servicios el '' indica que apunta a la raiz o se a ala misma carpeta
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # a url patterns le agrego la ruta estatica de la imagen