#Definir funciones

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")

        
#Programa principal

numero = int(input("Ingrese un numero entero: "))
tabla_multiplicar(numero)