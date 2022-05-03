from django.db import models

# Create your models here.


from django.db import models

from django.utils import timezone

from django.db import models
from django.utils import timezone
#from six import string_types
import datetime

from django.contrib.auth.models import User

    def __str__(self):
        return self.genero

class Subgenero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

class Subgenero2(models.Model):
    genero = models.CharField(max_length=100)
    def __str__(self):
        return self.genero

class Questao(models.Model):
 questao_texto =models.CharField(max_length=200)
 pub_data =models.DateTimeField('data de publicacao')

 def __str__(self):
  return self.questao_texto

 def foi_publicada_recentemente(self):
  return self.pub_data >= timezone.now() - datetime.timedelta(days=1)


class Opcao(models.Model):
 questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
 opcao_texto = models.CharField(max_length=200)
 votos = models.IntegerField(default=0)

 def __str__(self):
  return self.opcao_texto





class Aluno(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 curso = models.CharField(max_length=100)


#exemplo
 '''
  omeuuser = User.objects.create_user('Maria',
                                      'maria@iscte.pt',
                                      'passdemar')
  ut = Aluno(user=omeuuser, curso='LIGE')
  ut.user.username

  u = User.objects.get(username='jose')
  cursoDoJose = u.aluno.curso
 '''


