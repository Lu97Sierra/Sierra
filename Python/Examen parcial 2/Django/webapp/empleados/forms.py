from django.forms import ModelForm
from empleados.models import Empleado

class empleadoform(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'