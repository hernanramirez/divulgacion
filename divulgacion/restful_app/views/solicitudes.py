import operator
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from functools import reduce

from intranet.solicitudes_app.models import Constancia
from intranet.restful_app.serializers.solicitudes import ConstanciaSerializer


class ConstanciasList(generics.ListCreateAPIView):

    required_groups = {
        'GET': ['ClientUser'],
        'POST': ['ClientUser'],
    }
    #permission_classes = (IsAuthenticated, HasGroupPermission,)

    serializer_class = ConstanciaSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Constancia.objects.filter(empleado=user)[:10]


class ConstanciaDetail(generics.RetrieveUpdateDestroyAPIView):
    required_groups = {
        'GET': ['Administrator'],
        'POST': ['Administrator'],
    }
    #permission_classes = (IsAuthenticated, HasGroupPermission,)

    queryset = Constancia.objects.all()
    serializer_class = ConstanciaSerializer
