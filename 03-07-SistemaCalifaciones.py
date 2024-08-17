while True:
    try:
        valor = float(input('Proporciona un valor entre 0 y 10: '))
        mensaje = ''
        if 9 <= valor <= 10:
            mensaje = 'A'
        elif 8 <= valor < 9:
            mensaje = 'B'
        elif 7 <= valor < 8:
            mensaje = 'C'
        elif 6 <= valor < 7:
            mensaje = 'D'
        elif 0 <= valor < 6:
            mensaje = 'F'
        else:
            mensaje = 'Valor incorrecto'
        print(mensaje)

    except KeyboardInterrupt:
        break
    except ValueError:
        continue
