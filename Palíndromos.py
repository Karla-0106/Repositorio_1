"""
Programa echo en Pyton que 
indica al usuario si es 
Palindromo o no, e imprime 
"""
def es_palindromo(palabra):  # Esta funcion ayuda a definir si es o no palindromo
    palabra = palabra.replace(" ", "").lower() #Elimina los espacios en blanco 
    reverso = palabra[::-1] #Generamos esta palabra por si la palabra esta al reverso
    return palabra == reverso

texto = input("Ingresa una palabra o frase: ") #Ayuda a pedirle al usuario la palabra y la almacena
if es_palindromo(texto): #Estas lineas de condicion audan a imprimir al usuario 
    print("¡Es un palíndromo!") #Si es o no palindromo la palabra
else:
    print("No es un palíndromo.")
