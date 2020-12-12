from django.urls import path

from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'), #Aca se setean los parametros de busqueda y redirige
    path('detail/<str:pID>/<str:filterEValue>/<int:filterConservationPersentage1>/<int:filterConservationPersentage2>', views.homologyDetailView, name='homology-detail'),
]