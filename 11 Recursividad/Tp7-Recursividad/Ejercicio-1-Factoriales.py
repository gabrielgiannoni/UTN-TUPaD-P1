#Funcion recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)

def factorial_iterativo(limite):
    
    for i in range(1, limite + 1):
        
        print(F"F!{i} = {factorial(i)}")
        
    return 

# #Programa principal

limite = int(input("Ingrese un numero entero: "))

factorial_iterativo(limite)


# Cómo funciona:
# La función factorial(n) se llama a sí misma hasta llegar a n == 1 o n == 0.

# El usuario ingresa un número.

# Un bucle for recorre los números del 1 hasta el número ingresado.

# Para cada número, calcula y muestra su factorial.