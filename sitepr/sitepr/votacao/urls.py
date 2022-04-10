from django.urls import include, path
from . import views





app_name = 'votacao'
urlpatterns = [
 # ex: votacao/
 path("", views.index, name='index'),
 # ex: votacao/1
 path('<int:questao_id>', views.detalhe, name='detalhe'),
 # ex: votacao/3/resultados
 path('<int:questao_id>/resultados', views.resultados, name='resultados'),
 # ex: votacao/5/voto
 path('<int:questao_id>/voto', views.voto, name='voto'),



 path('criarQuestao', views.criarQuestao, name='criarQuestao'),

 path('gravaquestao', views.gravaquestao, name='gravaquestao'),

 path('<questao_id>/novaopcao/', views.nova_opcao, name='nova_opcao'),
 path('<questao_id>/nova_opcaoid', views.nova_opcaoid, name='nova_opcaoid'),
 #mudei
path('<int:questao_id>/apagaOpcao', views.apagaOpcao, name='apagaOpcao'),
path('criarUser', views.criarUserPage, name='criarUser'),
 path('criarUserButton', views.criarUserButton, name='criarUserButton'),
path('<questao_id>/apagaQuestao', views.apagaQuestao, name='apagaQuestao'),
path('loginview', views.loginview, name='loginview'),
path('paginaInsucesso', views.paginaInsucesso, name='paginaInsucesso'),
path('paginaSucesso', views.paginaSucesso, name='paginaSucesso'),
path('paginaAdmin', views.paginaAdmin, name='paginaAdmin'),
path('logoutview', views.logoutview, name='logoutview'),
path('informacaoPessoal', views.informacaoPessoal,name='informacaoPessoal'),
]

