#Definimos funcion
def contar_digito(numero, digito):
    if numero == 0:
        return 0  # Caso base: ya no quedan más dígitos por revisar
    else:
        ultimo = numero % 10  # Tomamos el último dígito
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)  # Coincide: suma 1
        else:
            return contar_digito(numero // 10, digito)  # No coincide: sigue sin sumar

# Pruebas
print(contar_digito(12233421, 2))  # → 3
print(contar_digito(5555, 5))      # → 4
print(contar_digito(123456, 7))    # → 0  


# ¿Cómo funciona?
# numero % 10 obtiene el último dígito.

# numero // 10 elimina el último dígito.

# Si el último dígito coincide con el buscado, suma 1 y sigue la recursión.

# Si no, simplemente sigue la recursión.