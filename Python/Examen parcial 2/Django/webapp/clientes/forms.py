from django.forms import ModelForm
from clientes.models import Cliente

class clienteform(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'