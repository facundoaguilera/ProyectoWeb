from unicodedata import name
from django.urls import path
from . import views
from .views import VRegistro


urlpatterns = [         
    # path('',views.autenticacion,name='Autenticacion'),
    path('', VRegistro.as_view(),name='Auteticacion')
        
      ]