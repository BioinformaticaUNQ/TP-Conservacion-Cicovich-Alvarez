from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import controllers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homology/', include('homology.urls')),
    path('', RedirectView.as_view(url='/homology/', permanent=True)),
    path('fasta/<str:pID>', controllers.fasta, name='fasta'),
    path('clustal/<str:pID>/<str:filterEValue>', controllers.clustal, name='clustal'),
    path('conservation/<str:pID>/<str:filterEValue>/<int:filterConservationPersentage>', controllers.conservation, name='conservation'),
    path('conservation2/<str:pID>/<str:filterEValue>/<int:filterConservationPersentage>', controllers.conservation2, name='conservation2'),
]