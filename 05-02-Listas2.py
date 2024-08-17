names = ['Adolf', 'Putin', 'Cristina', 'Mao', 'Bush', 'Chavez']
print(names[0:5])

# Ir del inicio de la lista al indice sin incluirlo
print(names[:2])

# Desde el indice indicando hasta el final
print(names[1:])

# Cambias el valor
names[5] = 'Maduro'
print(names)

for n in names:
    print(n)
else:
    print('Fin del eje del mal.')

# Preguntar el largo de una lista
print(len(names), 'Fuerzas Malignas')

# Agregar un elemento
names.append('Peron')
print(names)

# insertar un elemento en un indice en especifio
names.insert(1,'Stalin')
print(names)

# Remover un elemento
names.remove('Peron')
print(names)

# Remover el ultimo valor agregado
names.pop()
print(names)

# Eliminar un indice
del names[5]
print(names)

# Limpiar la lista
names.clear()
print(names)

# Boorar la lista por completo
"""del names
print(names)"""