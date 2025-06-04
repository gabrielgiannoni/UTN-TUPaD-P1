#definiciones de funciones

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(f"La cantidad ingresada en segundos equivale a {horas:.2f} hs")
#Programa principal
segundos = int(input("Ingrese los segundos a calcular: "))
segundos_a_horas(segundos)