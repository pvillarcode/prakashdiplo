from django.shortcuts import render
from .models import MiModelo

def mi_vista(request):
    objetos = MiModelo.objects.all()
    return render(request, 'mi_template.html', {'objetos': objetos})
