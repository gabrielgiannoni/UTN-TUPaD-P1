#Definir funcion
def contar_bloques(n):
    if n == 1:
        return 1  
    else:
        return n + contar_bloques(n - 1)

# Pruebas
print(contar_bloques(1))  # → 1
print(contar_bloques(2))  # → 3 (2 + 1)
print(contar_bloques(4))  # → 10 (4 + 3 + 2 + 1)

# ¿Cómo funciona?

# Caso base: si n == 1, solo hay un nivel con 1 bloque.

# En el caso general, suma los bloques del nivel actual (n) con la cantidad de bloques 
# necesarios para los niveles superiores (n-1).

