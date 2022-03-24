from django.urls import path
from proyectoWebApp import views
from django.conf import settings #agrego el settings para llamar 
from django.conf.urls.static import static #agrego los archivos static

urlpatterns = [
    
    path('',views.home,name='Home'),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # a url patterns le agrego la ruta estatica de la imagen