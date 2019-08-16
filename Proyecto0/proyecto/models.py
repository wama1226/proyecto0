from django.db import models

#para crear formularios se puede crear un archivo forms.py pero es lo mismo si se hace por models, se crea el otro archivo para mantener cierta estructura
#para este caso se continua en models

# Create your models here.

CATEGORIAS_SELECCION=(
    ('conferencia','Conferencia'),
    ('seminario','Seminario'),
    ('congreso','Congreso'),
    ('curso','Curso'),
)
class Usuario(models.Model):
    nombres=models.CharField(max_length=64)
    apellidos=models.CharField(max_length=64)
    identificacion=models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=10)

    def __str__(self):
        return f" {self.email} {self.identificacion}"

class Evento(models.Model):
    #usuarios=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="evento")
    nombre=models.CharField(max_length=10)
    categoria=models.CharField(max_length=20, choices=CATEGORIAS_SELECCION, default='conferencia')
    lugar=models.CharField(max_length=10)
    direccion=models.CharField(max_length=10)
    fechaInicio=models.DateField()
    fechaFinal=models.DateField()
    presencial=models.BooleanField()

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
