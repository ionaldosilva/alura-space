from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografias
from django.contrib import messages

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
    return render(request, "galeria/buscar.html", {"cards": fotografia})

