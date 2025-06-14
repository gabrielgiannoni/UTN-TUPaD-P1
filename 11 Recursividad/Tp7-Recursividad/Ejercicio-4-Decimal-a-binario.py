#Definimos funciones
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
elif numero == 0:
    print("El número binario de 0 es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")
    
# Explicación:
# n // 2 divide el número entre 2 descartando el decimal.

# n % 2 da el resto, que será 0 o 1.

# La función se va llamando a sí misma con el cociente, y cuando llega a 0,
# empieza a construir la cadena binaria al “volver” de las llamadas recursivas.