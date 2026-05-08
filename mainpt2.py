from pt2empleado import Empleado
from empresa import Empresa

empresa=Empresa()

input("desea cargar un nuevo empleado? s/n: ")

op= "s"
while op=="s":
    nombre=input("ingrese un nombre: ")
    dni=int(input("ingrese un dni: "))
    sueldo=float(input("ingrese sueldo: "))




    emp= Empleado(nombre,dni,sueldo)
    
    cargado= empresa.registrarempleado(emp)
    if not cargado:
        print(f"Empleado {emp.nombre} DNI {emp.dni} con sueldo {emp.sueldo} cargado exitosamente")
    else:
        print(cargado)
    


    op=input("desea cargar un nuevo empleado? s/n: ")
    
print()   
print("Lista de empleados cargados exitosamente")
for empleado in empresa.empleados:
    print(f"nombre: {empleado.nombre}, dni: {empleado.dni}, sueldo{empleado.sueldo}")

print()
print()
maxs=empresa.maxsueldo()
print(f"El empleado {maxs.nombre} con DNI {maxs.dni} es quien posee el mayor sueldo: {maxs.sueldo}")

print()
print()

print(f"El sueldo promedio es {empresa.sueldoprom()}")
