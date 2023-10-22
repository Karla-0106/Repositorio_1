# Programa de Numeros Primos #

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Obtener el rango de números del usuario
inicio = int(input("Ingrese el numero inicial del rango: "))
fin = int(input("Ingrese el numero final del rango: "))

# Mostrar los números primos en el rango dado
print("Numeros primos en el rango:")
for num in range(inicio, fin + 1):
    if es_primo(num):
        print(num)
