#Definir funciones

def calcular_imc(peso_kg, altura_m):
    imc = peso_kg / (altura_m ** 2)
    return imc

#Programa principal
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))
imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}")
