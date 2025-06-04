#Definir funciones

def funcion_sumar(num1,num2):
    return num1 + num2

def funcion_restar(num1,num2):
    if num1<num2:
        resta = num2 - num1
    return resta

def funcion_multiplicar(num1,num2):
    return num1 * num2

def funcion_dividir(num1, num2):
    if num1<num2:
        division = num2 / num1
    return division

def operaciones_basicas(num1,num2):
    suma = funcion_sumar(num1,num2)
    resta = funcion_restar(num1,num2)
    multiplicar = funcion_multiplicar(num1,num2)
    dividir = funcion_dividir(num1,num2)

    print(f"La suma de los numero es: {suma}")
    print(f"La resta de los numero es: {resta}")
    print(f"La multiplicacion de los numero es: {multiplicar}")
    print(f"La division de los numero es: {dividir}")
    
#Programa principal
numero1 = int(input("Ingrese el numero1: "))
numero2 = int(input("Ingrese el numero2: "))
operaciones_basicas(numero1, numero2)