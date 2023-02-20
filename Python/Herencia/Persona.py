class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre=nombre
        self._edad=edad

    def __str__(self) -> str:
        return f'Persona: {self._nombre} , Edad:{self._edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto) -> None:
        super().__init__(nombre, edad)
        self._puesto = puesto
    def __str__(self) -> str:
        return f"{super().__str__()} Sueldo {self._puesto}"

        
