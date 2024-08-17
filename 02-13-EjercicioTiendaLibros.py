while True:
    try:
        print('Proporciona los siguientes datos del libro')
        nombre = input('Proporciona el nombre del libro: ')
        idLibro = int(input('Proporciona el ID del libro: '))
        precio = float(input('Proporciona el precio del libro: '))
        envioGratuito = input('Envio gratuito?: ').capitalize()

        if envioGratuito == 'True':
            envioGratuito = True
        elif envioGratuito == 'False':
            envioGratuito = False
        else:
            print('Valor incorrecto, debe escribir True/False')

        print(f'''
        Nombre: {nombre}
        ID: {idLibro}
        Precio: {precio}
        envioGratis: {envioGratuito}
        ''')

    except ValueError as e:
        print(f'Error: {e}. \nAsegúrate de ingresar valores válidos.')
    except Exception as e:
        print(f'Error inesperado: {e}.')
    except KeyboardInterrupt as k:
        break
