from django.urls import path
from.views import contacto, home, galeria

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('galeria', galeria, name="galeria"),
]