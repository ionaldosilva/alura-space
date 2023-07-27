from django.urls import path
from usuarios.views import Login, Cadastro, Logout

urlpatterns = [
    path('login', Login, name='login'),
    path('cadastro', Cadastro, name='cadastro'),
    path('logout', Logout, name='logout')

]