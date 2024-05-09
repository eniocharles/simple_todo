from django.forms import ModelForm  
from app.models import Pedidos
from django import forms


class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__' #Não precisa fazer uma lista com as fields da tabela pedidos, so usar o __all__ que ja puxa tudo do bd
        widgets = { #aki é pra na hora da interface do usuario ter a parte de horario igual o datetime do html
            'horario': forms.DateTimeInput(attrs={'type': 'time'}),}