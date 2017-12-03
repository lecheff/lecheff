from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cardapio/', views.prato_list, name='cardapio'),
    url(r'^galeria/', views.galeria, name='galeria'),
]
