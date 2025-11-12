from django.shortcuts import render

def members(request):
    # Renderiza la página informativa de Django
    return render(request, 'myfirst.html')