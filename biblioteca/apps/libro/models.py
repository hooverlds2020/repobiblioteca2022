from tabnanny import verbose
from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres', max_length = 200, blank = False, null = False)
    apellidos = models.CharField('Apellidos',max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 100, blank = False, null = False)
    #descripcion = models.TextField('Descripción', blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length=200, blank = True, null = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length= 255, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo

