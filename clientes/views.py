from django.shortcuts import render,redirect,get_object_or_404
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



def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:lista')
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})
