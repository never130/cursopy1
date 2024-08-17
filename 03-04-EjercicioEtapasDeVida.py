"""
Proporciona tu edad:
0-10: La infancia es increible...
10-20: Muchos cambios y mucho estudio...
20-30: Amor y comienza el trabajo...
Cualquier otro valor: Etapa de vida no reconocida.
"""
while True:
    try:
        miEdad = int(input('Proporciona tu edad: '))
        mensaje = None
        if 0 <= miEdad <= 10:
            mensaje = 'La infancia es incredible.'
        elif 10 <= miEdad <= 20:
            mensaje = 'Muchos cambios y mucho estudio.'
        elif 20 <= miEdad <= 30:
            mensaje = 'Amor y comienza el trabajo.'
        else:
            mensaje = 'Etapa de vida no reconocida.'
        print(f'Tu edad es {miEdad}. {mensaje}')

    except KeyboardInterrupt:
        break
    except ValueError:
        print('Error de valor. Reintentando...')
        continue
