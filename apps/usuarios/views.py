from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def Login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():

            id_login = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username=id_login,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{id_login} logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar login.")
                return redirect('login')
            

    return render(request,'Usuarios/login.html', {'form': form})

def Cadastro(request):
    cadastro = CadastroForms()

    if request.method == 'POST':
        cadastro = CadastroForms(request.POST)

        if cadastro.is_valid():
            
            nome=cadastro["nome_cadastro"].value()
            email=cadastro["email"].value()
            senha=cadastro["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário Existente")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(

                username=nome,
                email=email,
                password=senha
            )   
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')

    return render(request, 'Usuarios/cadastro.html', {'cadastro': cadastro})

def Logout(request):

    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect('login')


