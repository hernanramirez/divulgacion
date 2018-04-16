
import operator
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from functools import reduce

from rest_framework.response import Response

from intranet.users.models import Empleado
from intranet.restful_app.serializers.profile import UserSerializer
from rest_framework.views import APIView


class CurrentUserView(APIView):

    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
