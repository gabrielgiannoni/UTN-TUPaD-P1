#Definir funciones

def celsius_a_farenheit(celsius):
    return (celsius * 9/5)  + 32 


#Programa principal
celsius = float(input("Ingrese una temperatura en grados celsius: "))
farenheit = celsius_a_farenheit(celsius)
print(f"La temperatura en grados farenheit es: {farenheit}ºF")