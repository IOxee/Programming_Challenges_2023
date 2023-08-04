# Name: An�lisis de texto 
# Path: solution.py
# Author: IOxee
# TimeStamp: 04-08-2023 13:20:26

def analizar_texto(texto):
    # Inicializamos variables para el análisis
    num_palabras = 0
    longitud_total_palabras = 0
    num_oraciones = 0
    palabra_mas_larga = ""

    for palabra in texto.split():
        num_palabras += 1
        longitud_total_palabras += len(palabra)
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    longitud_media_palabras = longitud_total_palabras / num_palabras

    num_oraciones = texto.count('.')

    return num_palabras, longitud_media_palabras, num_oraciones, palabra_mas_larga

# Ejemplo de texto para analizar
texto_ejemplo = input("Ingresa un texto para analizar: ")
#texto_ejemplo = "Nos encontramos en un periodo de guerra civil. Las naves espaciales rebeldes, atacando desde una base oculta, han logrado su primera victoria contra el malvado Imperio Galáctico. Durante la batalla, los  espías rebeldes han conseguido apoderarse de los planos secretos del arma total y definitiva del Imperio, la ESTRELLA DE LA MUERTE, una estación espacial acorazada, llevando en sí potencia suficiente para destruir a un planeta entero. Perseguida por los  siniestros agentes del Imperio, la Princesa Leia vuela hacia su patria, a bordo de su nave espacial, llevando consigo los planos robados, que pueden salvar a su pueblo y devolver la libertad a la galaxia...."

# Llamamos a la función y mostramos los resultados
num_palabras, longitud_media_palabras, num_oraciones, palabra_mas_larga = analizar_texto(texto_ejemplo)

print("Número total de palabras:", num_palabras)
print("Longitud media de las palabras:", longitud_media_palabras)
print("Número de oraciones:", num_oraciones)
print("Palabra más larga:", palabra_mas_larga)
