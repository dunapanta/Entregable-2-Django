from django.contrib import admin

# Register your models here.
from clases.models import Estudiante, Clase

admin.site.register(Estudiante)
admin.site.register(Clase)