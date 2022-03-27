from django.db import models



# Create your models here.
class Empresa(models.Model):   #tabla
    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()

    #La tabla va a tener columnas y cada columna va a tener variables y datos
    #Para que los cambios en las tablas tengan efecto, 
    # hay que volver a la consola en la carpeta del proyecto 
    # y escribir el comando python manage.py makemigrations
    def __str__(self):
        return self.nombre