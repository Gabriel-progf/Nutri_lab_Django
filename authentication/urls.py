from django.urls import path
from . import views
urlpatterns = [
    
    path('cadastre/', views.cadastre, name="cadastre"),
    path('login/', views.login, name="login"),
    path('sair/', views.sair, name="sair"),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta")

    
]
