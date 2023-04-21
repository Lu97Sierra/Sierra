from django.forms import ModelForm
from productos.models import Producto

class productoform(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'