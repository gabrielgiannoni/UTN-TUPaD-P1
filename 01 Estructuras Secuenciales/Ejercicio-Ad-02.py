# Conversion de grados Celsius a Fahrenheit

# Objetivo : Realizar la conversion de temperatura de Celsius a Fahrenheit

# Instrucciones: 
# 1. Solicitar al usuario una temperatura en grados Celsius
# 2. Convertirla a Fahrenheit con la formula: F=(C*9/5) + 32.
# 3. Mostrar el resultado en pantalla

# Pedimos los datos al usuario

celsius = int(input("Ingrese una temperatura en grados Celsius: "))

# Convertimos a Fahrenheit

fahrenheit = (celsius*9/5) + 32

# Mostramos en pantalla

print(f"La temperatura ingresada convertida a grados fahrenheit es igual a: {fahrenheit}º")
