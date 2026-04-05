from django.views.generic import ListView, CreateView
from .models import Autor, Articulo

class AutorListView(ListView):
    model = Autor
    template_name = 'autores/list.html'

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'email']
    success_url = '/autores/'


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulos/list.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ['titulo', 'contenido', 'fecha_publicacion', 'autor']
    success_url = '/articulos/'