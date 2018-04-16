from django.conf.urls import url

from intranet.restful_app.views import marcas
from intranet.restful_app.views import recibos
from intranet.divulgacion_app.views import api
from intranet.restful_app.views import profile
from intranet.restful_app.views import solicitudes

urlpatterns = [

    url(
        regex=r'^current/$',
        view=profile.CurrentUserView.as_view(),
        name='current_user'
    ),

    # Recibos

    url(
        regex=r'^marcas/$',
        view=marcas.MarcaApiList.as_view(),
        name='recivos_list'
    ),

    # Marcas

    url(
        regex=r'^recibos/$',
        view=recibos.RecibosList.as_view(),
        name='recibod_list'
    ),

    url(
        regex=r'^solicitudes/constancias/$',
        view=solicitudes.ConstanciasList.as_view(),
        name='solicitudes_constancias_list'
    ),

    url(
        regex=r'^solicitudes/constancias/(?P<pk>\d+)$',
        view=solicitudes.ConstanciaDetail.as_view(),
        name='solicitudes_constancias_detail'
    ),

    # Constancias


]
