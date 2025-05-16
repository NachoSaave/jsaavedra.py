def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la resta es", n1-n2)
def division():
    try:
        n1=int(input("Ingrese un numero"))
        n2=int(input("Ingrese otro numero"))
        print("El resultado de la division es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepcion: {nombre_de_excepcion}")
def multiplicacion():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la multiplicacion es", n1*n2)
def calcu():
    while True:
        op=int(input('''Ingrese una opción
                    1.- Suma
                    2.- Resta
                    3.- Multiplicacion
                    4.- Division
                    5.- Salir'''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicación")
                multiplicacion()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")

calcu()