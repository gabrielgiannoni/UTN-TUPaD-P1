#Definir funciones

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1 # caso base
    else:
        return base * calcular_potencia(base, exponente - 1)
    
#Programa principal

base = int(input("Ingrese la base: "))

exponente = int(input("Ingrese el exponente (entero no negativo): "))

resultado = calcular_potencia(base, exponente)
print(f"{base} ^ {exponente} = {resultado}")