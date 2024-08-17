edadAdulto = 18
while True:
    try:
        edadPersona = int(input("Proporciona tu edad: "))
        if edadPersona >= edadAdulto:
            print(f'La persona con edad {edadPersona} es un adulto.')
        else:
            print(f'La persona con edad {edadPersona} es menor de edad.')
    except KeyboardInterrupt:
        print("\n¡Adiós!")
        break
  