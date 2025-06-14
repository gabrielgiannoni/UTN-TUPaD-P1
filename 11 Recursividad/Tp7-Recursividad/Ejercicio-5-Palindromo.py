#Definimos funcion

#Un palíndromo es una palabra, frase o número que se lee igual de izquierda a derecha
# que de derecha a izquierda, ignorando espacios, tildes, y signos de puntuación.

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin la primera y última letra
    return es_palindromo(palabra[1:-1])

#Programa principal
texto = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

if texto.isalpha(): #.isalpha()es un método que se aplica a cadenas de texto y 
                    # sirve para verificar si todos los caracteres de esa cadena son letras del alfabeto 
                    # (sin incluir espacios, números ni símbolos). 
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")
else:
    print("Por favor, ingresa solo letras (sin espacios, números ni caracteres especiales).")
    

# ¿Cómo funciona?
# Caso base: Si la palabra tiene 0 o 1 carácter → es palíndromo.

# Compara el primer y último carácter.

# Si son iguales, sigue llamando a la función con el resto de la palabra.

# Si no son iguales, devuelve False.