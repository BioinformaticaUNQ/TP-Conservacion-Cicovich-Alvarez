from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import controllers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homology/', include('homology.urls')),
    path('', RedirectView.as_view(url='/homology/', permanent=True)),
    path('fasta/<str:pk>', controllers.fasta, name='fasta'),
    path('clustal/<str:pk>', controllers.clustal, name='clustal'),
]