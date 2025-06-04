#Definicion funciones

def informacion_personal(nombre,apellido,edad,residencia):
    return print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
                  
#programa principal


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
