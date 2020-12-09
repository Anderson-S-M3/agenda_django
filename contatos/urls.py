from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_contatos'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.detalhe_contato, name='detalhe_contato'),
    path('criar_contato/', views.criar_contato, name='criar_contato'),
]
