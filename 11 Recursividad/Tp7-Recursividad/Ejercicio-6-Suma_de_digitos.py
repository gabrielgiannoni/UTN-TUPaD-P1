#Definimos funcion
def suma_digitos(n):
    if n < 10:
        return n 
    else:
        return (n % 10) + suma_digitos(n // 10)  # Último dígito + llamada recursiva con el resto

# Pruebas
print(suma_digitos(1234))  # → 10
print(suma_digitos(9))     # → 9
print(suma_digitos(305))   # → 8

# ¿Cómo funciona?
# n % 10 → obtiene el último dígito del número.

# n // 10 → elimina el último dígito (divide entre 10 sin decimales).

# La función se llama a sí misma con el número reducido hasta que queda solo un dígito.