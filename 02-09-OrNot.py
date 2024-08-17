vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer (Operador Or)')

if not (vacaciones or diaDescanso):
    print('Puede asistir al juego (Operador Not)')
else:
    print('Tiene deberes por hacer')
