import Rectangulo as rec

miRectangulo = rec.Rectangulo(5,10)
miRectangulo._ancho = 7
miRectangulo._largo = 10
print(miRectangulo._ancho)
print(miRectangulo._largo)
miRectangulo.CalcularArea()
print(miRectangulo._area)
print(miRectangulo.Perimetro())

miCuadrado = rec.Cuadrado(6)
print(miCuadrado.Area())
print(miCuadrado.Perimetro())