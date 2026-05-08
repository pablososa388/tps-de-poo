from datetime import time
from turnos import Turnos
from cancha import Cancha



cancha1=Cancha(1, "Césped")
cancha2=Cancha(2, "Cemento")
cancha3=Cancha(3, "Césped")

canchas = [cancha1, cancha2, cancha3]

print("1- Ver el estado actual de las 3 canchas (horarios libres y ocupados)")
print("2- Registrar reserva")
print("3- Cancelar reserva existente")

op=input("Ingrese la accion que desea realizar")

match op:
    case 1:
        for cancha in canchas:
            print(cancha)
