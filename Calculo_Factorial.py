# Programa que tiene una funcion para calcular factoriales #

# Función para calcular el factorial de un número dado
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Obtener el número del usuario
numero = int(input("Ingrese un numero: "))

# Calcular y mostrar el factorial del número
factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")
