from django.contrib import admin
from .models import Administrador, ComentariosDeNoticias, Usuario, Socio, DocDescargas, CursosYcapacitaciones, Consulta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Socio)
admin.site.register(DocDescargas)
admin.site.register(CursosYcapacitaciones)
admin.site.register(ComentariosDeNoticias)
admin.site.register(Administrador)

