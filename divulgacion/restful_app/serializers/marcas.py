from rest_framework import serializers
from intranet.asistencia_app.models import Marca


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = ('id', 'id_user', 'dispositivo', 'start', 'title')
