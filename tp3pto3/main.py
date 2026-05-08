from seeder import inicializarDatos
from continente import Continente
from pais import Pais
from provincia import Provincia


america, europa = inicializarDatos()
while True:
    print("1- Listar paises de un continente")
    print("2- Listar provincias de un país")
    print("3- Listar los paises límitrofes de un país")
    print("4- Listar todos los paises ordenados por superficie (mayor a menor)")
    print("5- Comparar 2 países por nombre e imprimir cuál tiene mayor superficie.")
    print("6- Salir del menú")

    op=input("Ingrese la opción que desee: ")
    match op:
        case "1":
            continentes=input("Ingrese un continente para listar sus países (América o Europa): ")
            if continentes.lower()=="america":
                continente=america
            elif continentes.lower()=="europa":
                continente=europa
            else:
                print("Continente no encontrado")
            
            print(f"Países de {continente.nombre}: ")
            for pais in continente.paises:
                print (pais.nombre)
        case "2":
            paisbusc=input("Ingrese un país para listar sus provincias: ")
            
            buscado= None

            for pais in america.paises + europa.paises:
                if pais.nombre.lower()==paisbusc.lower():
                    buscado= pais
                    break
            if buscado:
                print(f"Provincias de {buscado.nombre}:")
                for provincia in buscado.listadeprovincias:
                    print (provincia.nombre)
            else:
                print(f"{paisbusc} no encontrado")
        case "3":
            limitrofes=input("ingrese el país del cual desea saber sus limítrofes: ")

            buscado= None
            for pais in america.paises + europa.paises:
                if pais.nombre.lower()==limitrofes.lower():
                    buscado= pais
                    break
            if buscado:
                print(f"Países limítrofes de {buscado.nombre}")
                for limitrofes in buscado.paiseslimitrofes:
                    print(limitrofes.nombre)
            else:
                print(f"{limitrofes.nombre} no ha sido encontrado")
        case "4":
            print("Lista ordenada de países según su superficie en km^2 de mayor a menor: ")

            listaordenada= sorted(america.paises + europa.paises, key=lambda pais:pais.superficie, reverse=True)
            for paises in listaordenada:
                print(f"{paises.nombre}: {paises.superficie} km^2")
        case "5":
            while True:
                comparado=input("Ingrese un país a comparar: ")
                buscado= None
                for pais in america.paises + europa.paises:
                    if pais.nombre.lower()==comparado.lower():
                        buscado=pais
                        break
                if buscado:
                    break
                else: print(f"{comparado} no se encontró, intente de nuevo")
            while True:
                comparado2=input("Ingrese el segundo país a comparar: ")
                buscado2= None
                for pais2 in america.paises+ europa.paises:
                    if pais2.nombre.lower()==comparado2.lower():
                        buscado2=pais2
                        break
                if buscado2==buscado:
                    print("Usted ingresó el mismo país, ingrese otro")
                    continue


                elif buscado2:
                    break
                else: print(f"{comparado2} no se encontró, intente de nuevo")
            if buscado.superficie>buscado2.superficie:
                    print(f"Entre {comparado} y {comparado2}, quien tiene mayor superficie es: {buscado.nombre} con {buscado.superficie}km^2")
            elif buscado.superficie<buscado2.superficie:
                    print(f"Entre {comparado} y {comparado2}, quien tiene mayor superficie es: {buscado2.nombre} con {buscado2.superficie}km^2")
            else:
                    print(f"La superficie de {comparado} y {comparado2} es la misma")
        case "6":
            break
        case _:
            print("Opción inválida")




