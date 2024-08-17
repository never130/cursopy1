num = int(input('Proporciona un valor entre 1 y 3: '))
numText = ''
if num == 1:
    numText = 'Numero uno'
elif num == 2:
    numText = 'Numero dos'
elif num == 3:
    numText = 'Numero tres'
else:
    numText = 'valor fuera de rango'
print(f'Numero proporcionado: {num} - {numText}')
