#Definir funciones

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def serie_completa(limite):
    
    for i in range(limite + 1):
        
        print(F"F({i}) = {fibonacci(i)}")

    return
#Programa principal

limite = int(input("Ingrese un numero entero: "))

serie_completa(limite)

# ¿Cómo funciona?
# fibonacci(n) calcula el valor de la serie en la posición n.

# La función se llama a sí misma con n-1 y n-2 hasta llegar a los casos base (0 o 1).

# El for imprime desde la posición 0 hasta la que indicó el usuario.