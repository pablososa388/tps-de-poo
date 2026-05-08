from tpn3 import Entero


n1=Entero(11)
n2=Entero(10)


if n2.esPrimo():
    print(f"{n2.numero} es primo")
else:
    print(f"{n2.numero} no es primo")


if n1.esImpar():
    print(f"{n1.numero} es impar")
else:
    print(f"{n1.numero} es par")


if n2.esPar():
    print(f"{n2.numero} es par")
else:
    print(f"{n2.numero} es impar")


