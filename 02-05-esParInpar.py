while True:
    try:
        a = int(input('Escribe un valor numerico: '))
        print(a % 2)
        if a % 2 == 0:
            print(f'{a} es numero par.')
        else:
            print(f'{a} es numero impar.')
    except KeyboardInterrupt:
        print("\n¡Adiós!")
        break
