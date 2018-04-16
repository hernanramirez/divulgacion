
from divulgacion.divulgacion_app.models import Noticia
from divulgacion.divulgacion_app.serializer import NoticiaSerializer
from rest_framework import generics


class NoticiasRestList(generics.ListCreateAPIView):

    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class NoticiaRestDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
