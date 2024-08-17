# Califica tu dia del 1 al dia
dia = int(input('Como estuvo tu dia (1 al 10): '))
print('Mi dia estuvo de:', dia)


"""
Se solicita incluir la siguiente informacion acerca de un libro:
Titulo, autor.
Debes imprimir la informacion en el siguiente formato:
Proporciona el titulo:
Proporciona el autor:
<titulo> fue escrito por <autor>
"""
titulo = input('Proporciona el titulo: ')
autor = input('Proporciona el autor: ')
libro = f'El {titulo} fue escrito por {autor}.'
print(libro)
