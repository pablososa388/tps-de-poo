from datetime import time
from turnos import Turnos
from cancha import Cancha



cancha1=Cancha(1, "Césped")
cancha2=Cancha(2, "Cemento")
cancha3=Cancha(3, "Césped")

canchas = [cancha1, cancha2, cancha3]
while True:
    print("1- Ver el estado actual de las 3 canchas (horarios libres y ocupados)")
    print("2- Registrar reserva") 
    print("3- Cancelar reserva existente")
    print("4- Salir")

    op=input("Ingrese la accion que desea realizar ")

    match op:
        case "1":
            for cancha in canchas:
                print(cancha)

    match op:
        case "2":
            op1 = input("Ingrese el número de cancha (1, 2 o 3): ")
            while op1!="":
                if op1 == "1":
                    cancha = cancha1
                elif op1 == "2":
                    cancha = cancha2
                elif op1 == "3":
                    cancha = cancha3
                else:
                    print("Cancha inválida")
                    continue
                
                print(cancha)  # muestra estado actual
                hora = int(input("Ingrese la hora deseada (14-23): "))
                nombre = input("Ingrese nombre y apellido: ")
                turno = Turnos(nombre, hora)
                if cancha.reservarturno(turno):
                    print("Reserva exitosa")
                else:
                    print("Error: Turno ocupado")
                op1=input(f"Si desea cargar otro turno, seleccione nuevamente la cancha (1,2 o 3), de lo contrario, presione enter: ")
    match op:
        case "3":
            op1 = input("Ingrese el número de cancha (1, 2 o 3): ")
            while op1!="":
                if op1 == "1":
                    cancha = cancha1
                elif op1 == "2":
                    cancha = cancha2
                elif op1 == "3":
                    cancha = cancha3
                else:
                    print("Cancha inválida")
                    continue
                
                print(cancha)  # muestra estado actual
                hora = int(input("Ingrese la hora a cancelar (14-23): "))
                hora_time = time(hora, 0)
                if cancha.cancelarturno(hora_time):
                    print(f"Turno de las {hora}hs cancelado exitosamente")
                else:
                    print("Error, no existe reserva en ese horario")
                op1 = input("Si desea cancelar otro turno ingrese la cancha (1,2,3), de lo contrario presione enter: ")



    match op:
        case "4":
            break
