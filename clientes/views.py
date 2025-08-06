from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
def lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})



def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()

    return render(request, 'clientes/nuevo_cliente.html', {'form': form})

