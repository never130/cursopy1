# Sintaxix de range (inicio, fin, incremento
# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir numeros divisibles por 3
# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimir
# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

for num in range(11):
    if num % 3 == 0:
        print(num)
else:
    print('Fin Ejercicio 1')

for num in range(2, 7):
    print(num)
else:
    print('Fin Ejercicio 2')

for num in range(3, 10, +2):
    print(num)
else:
    print('Fin Ejercicio 3')
