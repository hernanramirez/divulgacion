from rest_framework import serializers
from intranet.solicitudes_app.models import Constancia


class ConstanciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Constancia
        fields = ('__all__')
