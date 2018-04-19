#from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
#from pure_pagination.mixins import PaginationMixin

from divulgacion.divulgacion_app.models import Noticia

#aqui empieza la importacion de libreiras REST

#aqui termina la importacion de librerias REST


class NoticiaListView(LoginRequiredMixin, ListView):

    model = Noticia
    template_name = 'divulgacion_app/noticias/noticias_list.html'
    context_object_name = 'noticia_list'
    #paginate_by = 50

    page = {
        'title': 'Administrador',
        'subtitle': 'Noticias'
    }

    def get_context_data(self, **kwargs):
        context = super(NoticiaListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class NoticiaCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'titulo','resumen','empleado','contenido','imagen',
    ]

    model = Noticia
    template_name = 'divulgacion_app/noticias/noticias_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Creacion de las noticias'
    }

    def get_context_data(self, **kwargs):
        context = super(NoticiaCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    #def get_success_url(self):
    #    return reverse('divulgacionapp:noticia_list')


class NoticiaDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'titulo','resumen','empleado','contenido','fechareg','fechaact','imagen',

    ]

    model = Noticia
    template_name = 'divulgacion_app/noticias/noticias_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'Visualizacion de las noticias'
    }

    def get_context_data(self, **kwargs):
        context = super(NoticiaDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class NoticiaUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'titulo','resumen','empleado','contenido','imagen',
    ]

    model = Noticia
    template_name = 'divulgacion_app/noticias/noticias_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de las noticias'
    }

    def get_context_data(self, **kwargs):
        context = super(NoticiaUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    #def get_success_url(self):
    #    return reverse('divulgacionapp:noticia_list')


class NoticiaDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'titulo','resumen','empleado','contenido','fechareg','fechaact','imagen',
    ]

    model = Noticia
    template_name = 'divulgacion_app/noticias/noticias_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'eliminacion de la noticia'
    }

    def get_context_data(self, **kwargs):
        context = super(NoticiaDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    #def get_success_url(self):
    #    return reverse('divulgacionapp:noticia_list')
