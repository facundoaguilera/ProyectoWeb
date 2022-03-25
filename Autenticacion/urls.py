from unicodedata import name
from django.urls import path
from . import views
from .views import VRegistro, cerrarSesion, logear


urlpatterns = [         
    # path('',views.autenticacion,name='Autenticacion'),
    path('', VRegistro.as_view(),name='Autenticacion'),
    path('cerrarSesion',cerrarSesion,name='cerrarSesion'),
    path('logear',logear,name='logear'),  
      ]