from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
def saludo(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/saludo.html', {'clientes': clientes})


def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saludo')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/registrar.html', {'form': form})