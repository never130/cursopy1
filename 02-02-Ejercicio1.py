# Calcular el area y perimetro del cuadrado
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo '))
area = alto * ancho
factorPerimetro = 2
perimetro = (alto + ancho) * factorPerimetro
print(f'El area del rectangulo es {area} y el perimetro es {perimetro}')
