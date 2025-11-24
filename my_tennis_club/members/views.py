from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
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

def testing(request):
  mymembers = Member.objects.all().values()
  column_firstname = Member.objects.all().values_list('firstname')
  records_neymar = Member.objects.filter(firstname__icontains='Neymar').values()
  records_neymar_lamine = Member.objects.filter(Q(firstname='Neymar') | Q(firstname='Lamine')).values()
  endwith_s = Member.objects.filter(firstname__iendswith='s').values()
  contain_ez = Member.objects.filter(lastname__icontains='ez').values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'mymembers': mymembers,
    'column_firstname': column_firstname,
    'records_neymar': records_neymar,
    'records_neymar_lamine': records_neymar_lamine,
    'endwith_s': endwith_s,
    'contain_ez': contain_ez,
  }
  return HttpResponse(template.render(context, request))
