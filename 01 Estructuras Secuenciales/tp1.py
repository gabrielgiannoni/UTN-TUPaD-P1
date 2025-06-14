#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5 

segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
numero = int(input("Ingrese un numero entero: "))
print(f"La tabla de multiplicar del numero {numero} es: ")
print(f"{numero} por 1: {numero*1}")
print(f"{numero} por 2: {numero*2}")
print(f"{numero} por 3: {numero*3}")
print(f"{numero} por 4: {numero*4}")
print(f"{numero} por 5: {numero*5}")
print(f"{numero} por 6: {numero*6}")
print(f"{numero} por 7: {numero*7}")
print(f"{numero} por 8: {numero*8}")
print(f"{numero} por 9: {numero*9}")

#Ejercicio 7
numero1 = int(input("Ingrese un numero enteros distintos de 0: "))
numero2= int(input("Ingrese otro numero distinto de 0: "))
suma = (numero1 + numero2)
resta = (numero1 - numero2)
multiplicacion = (numero1 * numero2)
division = (numero1 / numero2)
print(f"Los numeros ingresados son {numero1} y {numero2}")
print(f"La suma de ambos numeros es {suma}")
print(f"La resta de ambos numeros es {resta}")
print(f"La multiplicacion de ambos numeros es {multiplicacion}")
print(f"La division de ambos numeros es {division}")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = (peso / (altura ** 2))
print (f"Su indice de masa corporal es: {imc}")

#Ejercicio 9
celsius = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print (f"La conversion de los {celsius} grados celsius a fahrenheit es: {fahrenheit} grados fahrenheit")

#Ejercicio 10
print("Ingrese 3 numeros: ")
numero1 = int(input("numero1: "))
numero2 = int(input("numero2: "))
numero3 = int(input("numero3: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los 3 numeros ingresados es: {promedio}")
