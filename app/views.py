from django.shortcuts import render, redirect 
from app.forms import PedidosForm #Criei com o uso do proprio django que disponibiliza o form, a minha função PedidosForm, que vai receber os parametros de um formulario
from app.models import Pedidos # Aki o banco de dados criado chamado Pedidos

def home(request): #Pagina Principal
    return render(request, 'home.html')

def pedidos(request): #Pagina dos pedidos que é o crud em si
    data = dict() #eu crio um dicionario
    data['db'] = Pedidos.objects.all() #e uma key no dicionario com o value sendo todos os objetos da tabela Pedidos do banco de dados
    return render(request, 'pedidos.html', data) #a request não so retorna a pagina, mas tem que retornar agr esse dicionario data

def form(request):
    data = dict()
    data['form'] = PedidosForm() # aki o data da função recebe uma key form que serve pra representar o formulario, por isso o value dela é o PedidosForm que a gente importou la em cima
    return render(request, 'form.html', data)

def create(request):
    form = PedidosForm(request.POST or None) #Pro create a gente usa o metodo post que serve resumidamente para criação, ou post ou nada tlgd
    if form.is_valid(): #na condição do form esta valido ele retorna um Form.save que significa que salvou e deu certo
        form.save()
        return redirect('pedidos') #Aqui ele faz um redirect(tipo redirecionar ou atualizar a pagina) pra url pedidos
    
def view(request, pk): #ele recebe o parametro pk para poder trabalhar com base naquela chave primaria que distingue cada um dos objetos
    data = dict()
    data['db'] = Pedidos.objects.get(pk=pk) #aki o data dele recebe uma key db que tem como value um metodo get(com parametro a pk) que serve de Read, visualização
    return render(request, 'view.html', data)

def edit(request, pk):
    data = dict()
    data['db'] = Pedidos.objects.get(pk=pk) #No edit ele vai ter outro db que dessa vez recebe o get de visualização mas para outra coisa, ver abaixo
    data['form'] = PedidosForm(instance=data['db']) #dentro da key form ele recebe o value PedidosForm com a instancia da key db do dicionario data
    return render(request, 'form.html', data) # aqui ele retorna a pagina form(que é a pagina de adicionar pedidos), tu vai saber pq no update e vendo a pagina html do form

def update(request, pk):
    data = dict()
    data['db'] = Pedidos.objects.get(pk=pk) #aqui ele tem outro get de visualização daquele objeto do banco que ele puxou pra dar o update
    form = PedidosForm(request.POST or None, instance = data['db']) #Aqui ele transforma o form em uma area de update, pegando o msm paramentro post or none de criação, so que com a instancia db que representa o objeto daquela vez
    if form.is_valid(): # novamente a condição de estar valido o formulario para passar
        form.save()
        return redirect('pedidos')

def delete(request, pk): #Aki é bem facil, pela pk do objeto selecionado
    db = Pedidos.objects.get(pk=pk) #ele vai no banco de dados diretamente po meio da pk do objeto e da um get de visualização nele pra usar dps
    db.delete() #com uma função propria do banco de dados ele dar um simples função delete
    return redirect('pedidos') #aki ele redireciona pro crud atualizado ou seja ele dar tipo um f5 na pagina dps de deletar o objeto