from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from divulgacion.divulgacion_app.models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):
    '''
    imagen = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    '''

    class Meta:
        model = Noticia
        fields = (
            'id',
            'titulo',
            'resumen',
            'empleado',
            'contenido',
            'fechareg',
            'fechaact'
            )
