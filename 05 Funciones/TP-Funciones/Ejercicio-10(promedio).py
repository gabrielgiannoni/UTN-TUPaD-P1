#Definir funciones

def calcular_imc(a, b, c):
    return ((a + b + c) / 3)

#Programa principal
a = float(input("Ingrese el numero 1: "))         
b = float(input("Ingrese el numero 2: "))
c = float(input("Ingrese el numero 3: "))
imc = calcular_imc(a, b, c)
print (f"El indice de masa muscular obtenido es: {imc}")