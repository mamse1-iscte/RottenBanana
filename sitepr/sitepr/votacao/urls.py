from django.urls import include, path
from . import views





# (. significa que importa views da mesma directoria)

app_name = 'votacao'

urlpatterns = [
 path("", views.index, name="index"),
 path('criaConta', views.criaConta, name='criaConta'),
 path('HomePage', views.HomePage, name='HomePage'),
 path('fazerLogin', views.fazerLogin, name='fazerLogin'),
 path('mostrarFilmes', views.mostrarFilmes, name='mostrarFilmes'),
 path('mostrarSeries', views.mostrarSeries, name='mostrarSeries'),
 path('criarUser', views.criarUserButton, name='criarUserButton'),
 path('boas', views.boas, name='boas'),

]