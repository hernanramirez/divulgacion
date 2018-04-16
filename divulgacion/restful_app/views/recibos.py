
import operator
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from functools import reduce

from intranet.recibos_app.models import Recibo
from intranet.restful_app.serializers.recibos import ReciboSerializer


class RecibosList(generics.ListCreateAPIView):

    required_groups = {
        'GET': ['ClientUser'],
        'POST': ['ClientUser'],
    }
    #permission_classes = (IsAuthenticated, HasGroupPermission,)

    serializer_class = ReciboSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Recibo.objects.filter(empleado=user)[:10]


