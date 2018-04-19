from django.conf.urls import url
from divulgacion.divulgacion_app.views.noticias import (
    NoticiaListView, NoticiaCreateView, NoticiaDetailView,
    NoticiaUpdateView, NoticiaDeleteView
)
from divulgacion.divulgacion_app.views.api import (
    NoticiasRestList, NoticiaRestDetail
)

urlpatterns = [
    url(
        regex=r'^noticia/$',
        view=NoticiaListView.as_view(),
        name='noticia_list'
    ),
    url(
        regex=r'^noticia/create/$',
        view=NoticiaCreateView.as_view(),
        name='noticia_create'
    ),
    url(
        regex=r'^noticia/view/(?P<pk>\d+)$',
        view=NoticiaDetailView.as_view(),
        name='noticia_view'
    ),
    url(
        regex=r'^noticia/update/(?P<pk>\d+)$',
        view=NoticiaUpdateView.as_view(),
        name='noticia_update'
    ),
    url(
        regex=r'^noticia/delete/(?P<pk>\d+)$',
        view=NoticiaDeleteView.as_view(),
        name='noticia_delete'
    ),
    url(
        regex=r'^api/noticias/$',
        view=NoticiasRestList.as_view(),
        name='noticia_rest_list'
    ),
    url(
        regex=r'^api/noticias/(?P<pk>\d+)$',
        view=NoticiaRestDetail.as_view(),
        name='noticia_rest_list'
    ),
]
