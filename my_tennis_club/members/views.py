from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render({}, request))

# Nueva vista para la guía de Django (usa base.html en myfirst.html)
def django_guide(request):
  return render(request, 'myfirst.html')

# Manejador personalizado para 404
# Se activará cuando DEBUG=False y la URL no exista
def custom_404(request, exception):
  # 404.html extiende master.html para mantener diseño del club
  return render(request, '404.html', status=404)
