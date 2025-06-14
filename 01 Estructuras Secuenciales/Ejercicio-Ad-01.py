# Calculo del area y el perimentro de un rectangulo

#Objetivo :  Calcular el area y el perimentro a partir de medidas dadas por el usuario

#Instrucciones :
#1. Pedir al usuario que ingrese el ancho y el alto de un rectangulo
#2. Calcular el area usando la formular: ancho * alto.
#3. Calcular el perimetro con la formula: (ancho*2)+(alto*2).
#4. Mostrar ambos resultados por pantalla


#Pedimos los datos al usuario

ancho = int(input("Ingrese el ancho del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))

#Calculamos el area

area = ancho * alto

#Calculamos el perimetro

perimetro = (ancho*2)+(alto*2)

#Mostramos los resultados por pantalla

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")