from django.conf.urls import url

from divulgacion.divulgacion_app.views import noticias
from divulgacion.divulgacion_app.views import api

urlpatterns = [
    url(
        regex=r'^noticia/$',
        view=noticias.NoticiaListView.as_view(),
        name='noticia_list'
    ),
    url(
        regex=r'^noticia/create/$',
        view=noticias.NoticiaCreateView.as_view(),
        name='noticia_create'
    ),

    url(
        regex=r'^noticia/view/(?P<pk>\d+)$',
        view=noticias.NoticiaDetailView.as_view(),
        name='noticia_view'
    ),

    url(
        regex=r'^noticia/update/(?P<pk>\d+)$',
        view=noticias.NoticiaUpdateView.as_view(),
        name='noticia_update'
    ),

    url(
        regex=r'^noticia/delete/(?P<pk>\d+)$',
        view=noticias.NoticiaDeleteView.as_view(),
        name='noticia_delete'
    ),

    url(
        regex=r'^api/noticias/$',
        view=api.NoticiasRestList.as_view(),
        name='noticia_rest_list'
    ),

    url(
        regex=r'^api/noticias/(?P<pk>\d+)$',
        view=api.NoticiaRestDetail.as_view(),
        name='noticia_rest_list'
    ),

]
