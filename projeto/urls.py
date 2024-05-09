from django.contrib import admin
from django.urls import path
#Aki tu vai importar do aplicativo o views.py onde vai ter todas as funções do site,
#algumas funções servem so para abrir uma pagina como a home, os pedidos(crud), a view e a edit
from app.views import home, pedidos, form, create, view, edit, update, delete  

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cada path vai gerar um url  para cada função, vai chamar o nome da url, depois o nome da função
    #que foi importado da app.views e depois o nome dela pra quando a gente for chamar uma url, so precisa do nome
    path('', home, name='home'),
    path('pedidos/', pedidos, name='pedidos'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    #todas esses paths de baixo para receber essas funções tem esse paramentro int:pk pra poder se relacionar
    #com aquele objeto da tabela tlgd, se eu for view ou edit o pedido da mesa 1 eu vou atras dele pela pk(chave primaria)
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]
