import math

#Definir funciones
def calcular_area_circulo(radio):
    area_circulo = math.pi * radio ** 2
    return print(f"El area del circulo es: {area_circulo}")

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * math.pi * radio
    return print(f"El perimetro del circulo es: {perimetro_circulo}")

#Programa principal
radio = float(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
