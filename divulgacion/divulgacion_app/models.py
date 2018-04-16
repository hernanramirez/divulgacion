from django.db import models
from versatileimagefield.fields import VersatileImageField

from intranet.users.models import Empleado


class Noticia(models.Model):
    titulo = models.CharField('Titulo de la noticia', max_length=70)
    resumen = models.TextField('Resumen de la noticia')
    empleado = models.ForeignKey(Empleado)
    contenido = models.TextField('Contenido de la noticia')
    fechareg = models.DateTimeField(auto_now_add=True)
    fechaact = models.DateTimeField(auto_now=True)
    imagen = VersatileImageField('imagen', upload_to='imagenes/', blank=True, null=True)
