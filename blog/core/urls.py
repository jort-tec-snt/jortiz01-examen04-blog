from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AutorListView.as_view()),
    path('autores/nuevo/', AutorCreateView.as_view()),
    path('articulos/', ArticuloListView.as_view()),
    path('articulos/nuevo/', ArticuloCreateView.as_view()),
]