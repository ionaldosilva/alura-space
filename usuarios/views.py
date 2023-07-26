from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request,'Usuarios/login.html', {'form': form})

def cadastro(request):
    cadastro = CadastroForms()
    return render(request, 'Usuarios/cadastro.html', {'cadastro': cadastro})


