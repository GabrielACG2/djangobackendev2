from django.shortcuts import render, redirect
from .models import EntradaCine
from .forms import EntradaCineForm

def listar_entradas(request):
    entradas = EntradaCine.objects.all()
    form = EntradaCineForm()

    if request.method == "POST":
        form = EntradaCineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrada-lista')
    return render(request, 'entrada/entrada_lista.html', {'entradas': entradas, 'form': form})

def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaCineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrada-lista')

    else:
        form = EntradaCineForm()

    return render(request, 'entrada/entrada_crear.html', {'form': form})

def editar_entrada(request, id):
    entrada = EntradaCine.objects.get(id=id)

    if request.method == 'POST':
        form = EntradaCineForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada-lista')
    else:
        form = EntradaCineForm(instance=entrada)
    return render(request, 'entrada/entrada_actualizar.html', {'entrada': entrada, 'form': form})


def eliminar_entrada(request, entrada_id):
    try:
        entrada = EntradaCine.objects.get(id=entrada_id)
        entrada.delete()
        return redirect('entrada-lista')
    except EntradaCine.DoesNotExist:
        pass

def pagina_principal(request):
    return render(request, 'todo.html')


