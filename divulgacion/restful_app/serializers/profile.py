from rest_framework import serializers
from intranet.users.models import Empleado, User
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from easy_thumbnails.fields import ThumbnailerImageField


class ThumbnailImageField(serializers.ImageField):
    """
    从 easy_thumbnails.fields.ThumbnailerImageField 字段类型中解析出缩略图信息
    """

    def __init__(self, *args, **kwargs):
        self.size_alias = kwargs.pop('size_alias', 'profile')
        self.source = kwargs.pop('source', 'foto')
        kwargs['read_only'] = True
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            return value[self.size_alias].url
        except Exception:
            return None


class EmpleadoProfileSerializer(serializers.HyperlinkedModelSerializer):

    foto = ThumbnailImageField()

    class Meta:
        model = Empleado
        fields = ('cedula','foto')



class UserSerializer(serializers.ModelSerializer):

    empleado = EmpleadoProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'empleado')

