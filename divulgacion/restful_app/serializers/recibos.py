from rest_framework import serializers
from intranet.recibos_app.models import Recibo

class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibo
        fields = ('id', 'descripcion', 'recibo_pdf',)
