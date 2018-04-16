
import operator
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from functools import reduce

from intranet.asistencia_app.models import Marca, EmpleadoClienteDispositivo
from intranet.restful_app.serializers.marcas import MarcaSerializer


class MarcaApiList(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)

    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_queryset(self):
        dis = EmpleadoClienteDispositivo.objects.filter(
            empleado_id=self.request.user.id)

        if not dis:
            return dis

        empleado_list = []

        for di in dis:
            empleado_list.append(Q(id_user=di.id_user))

        marcas = Marca.objects.filter(
            reduce(operator.or_, empleado_list)).order_by('-start')[:50]

        return marcas
