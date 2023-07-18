from django.contrib import admin
from .models import Pelicula, Director
# Register your models here.

class PeliculaInLine(admin.StackedInline):
    model = Pelicula
    extra = 1

class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields'('nombre', 'apellidos', 'biografia', 'imagen')}),
        ('Fechas',{
            'fields':('fecha_nacimiento', 'fecha_defuncion'),
            'classes':('collapse')
        })
    ]
    inLines = [PeliculaInLine]

admin.site.register(Director, DirectorAdmin)