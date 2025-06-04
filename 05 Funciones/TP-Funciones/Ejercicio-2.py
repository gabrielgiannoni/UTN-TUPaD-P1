#Definicion funciones
def saludar_usuario(nombre):
    return print(f"Hola {nombre}")


#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)