# Create your views here.

from .models import Filme_ou_serie, Genero, Comentario, Critico, Administrador, Subgenero, Subgenero2

from django.utils import timezone


from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



def index(request):
   # latest_question_list =Filme_ou_serie.objects.order_by('-pub_data')[:5]
   # context = {'latest_question_list':latest_question_list}
   return render(request, 'votacao/HomePage.html')

def boas(request):
    return render(request, 'votacao/boas.html')

def fazerLogin(request):
    return render(request, 'votacao/fazerLogin.html')





def criarUserButton(request):
    uploaded_file_url=''

    filepath = request.FILES.get('myfile', False)
    if request.method == 'POST' and filepath:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)



    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['psw']
    imagem=uploaded_file_url

    if User.objects.filter(username=username).exists():
        return HttpResponseRedirect(reverse('votacao:criaConta'))



    omeuuser = User.objects.create_user(username,email,password)
    ut = Critico(user=omeuuser,imagem=imagem)
    omeuuser.save()
    ut.save()
    user = authenticate(username=username, password=password)
    login(request, user)


    return HttpResponseRedirect(reverse('votacao:index'))



def loginview(request):
 username = request.POST['username']
 password = request.POST['psw']
 user = authenticate(username=username,
 password=password)




 if user is not None:
    login(request, user)
    if user.is_staff==1:
        return HttpResponseRedirect(reverse('votacao:administradorPage'))
    #paginaSucesso
    return HttpResponseRedirect(reverse('votacao:HomePage'))
 else:
    # paginaInsucesso(request)
     #paginaInsucesso
     return HttpResponseRedirect(reverse('votacao:fazerLogin'))



def informacaoPessoal(request):
    return render(request, 'votacao/informacaoPessoal.html')



def mudarImagemPerfil(request):
    current_user = request.user

    filepath = request.FILES.get('myfile', False)
    if request.method == 'POST' and filepath:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        Critico.objects.filter(user_id=current_user.id).update(imagem=uploaded_file_url)
    return render(request, 'votacao/informacaoPessoal.html')





def criaConta(request):
    return render(request, 'votacao/criaConta.html')

def mostrarSeries(request):
    return render(request, 'votacao/mostrarSeries.html')

def mostrarFilmes(request):
    return render(request, 'votacao/mostrarFilmes.html')

def HomePage(request):
    return render(request, 'votacao/HomePage.html')

def administradorPage(request):
    return render(request, 'votacao/administradorPage.html')



def criarFilme(request):
    imagem=''

    filepath = request.FILES.get('myfile', False)
    if request.method == 'POST' and filepath:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        imagem = uploaded_file_url



    if request.method == 'POST' :


        # se a invocação veio do form, isto é, está no 2º passo

        filme_texto = request.POST['nome_filme']
        genero = request.POST['genero']
        subgenero= request.POST['subgenero']
        subgenero2 = request.POST['subgenero2']
        filme_descricao = request.POST['filme_descricao']
        is_filme = request.POST['is_filme']
        anoLancamento= request.POST['anoLancamento']
        trailer = request.POST['trailer']


        if filme_texto:
            # se a questao_texto está preenchida,
            # então vai instanciar a Questão e depois volta ao detalhe
            generoObject=Genero.objects.get(pk=genero)
            generoObject1 = Subgenero.objects.get(pk=subgenero)
            generoObject2 = Subgenero2.objects.get(pk=subgenero2)
            filme = Filme_ou_serie(filme_texto = filme_texto, filme_ranking_critica = 0, filme_ranking_audiencia = 0, filme_descricao = filme_descricao,is_filme = is_filme, pub_data=timezone.now(), genero_id = generoObject ,release_year = anoLancamento, imagem = imagem,  subgenero2_id = generoObject2, subgenero_id = generoObject1 , trailer = trailer)
            filme.save()
            return HttpResponseRedirect(reverse('votacao:HomePage'))
        else:
            # se a questao_texto não está preenchida, volta ao form
            return HttpResponseRedirect(reverse('votacao:HomePage'))
    else:
         # se a invocação não veio do form, isto é, o 1º passo
        return render(request,'votacao/criarFilme.html')



def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('votacao:HomePage'))


def apagarFilmePage(request):
    return render(request, 'votacao/apagarFilme.html')

def editarFilmeSerie(request):
    return render(request, 'votacao/editarFilmeSerie.html')



def apagarFilme(request):
    #filme = get_object_or_404(Filme_ou_serie, pk=filme_id)
   # filme.delete()
    return HttpResponseRedirect(reverse('votacao:HomePage'))




