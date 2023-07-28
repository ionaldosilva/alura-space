from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografias
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado")
        return redirect('login')
    fotografia = Fotografias.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards':fotografia} )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografia = Fotografias.objects.order_by("data").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/index.html", {"cards": fotografia})

def nova_imagem(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = FotografiaForms
    if request.method=='POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia cadastrada com Sucesso!")
            return redirect('index')

    
    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    fotografia = Fotografias.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada com sucesso!")
            return redirect('index')
        
    return render(request, 'galeria/editar_imagem.html', {'form': form , 'foto_id': foto_id})
    

def deletar_imagem(request, foto_id):
    fotografia = Fotografias.objects.get(id=foto_id)
    fotografia.delete()
    return redirect('index')

def filtro(request, categoria):
    fotografia=Fotografias.objects.order_by("data").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {'cards':fotografia})

