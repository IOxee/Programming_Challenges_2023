import os


def heterograma(texto):
    # dividir el texto en letras y comprobar si hay repetidas si lo hay no es heterograma y se devuelve False
    texto = texto.lower()
    for letra in texto:
        if letra.isalpha():
            if texto.count(letra) > 1:
                return False
    
    return True

def isograma(texto):
    # Isogramas con una repetición o de segundo orden: acondicionar (11), escritura (9), intestinos (10), papelera (8).
    texto = texto.lower()
    for letra in texto:
        if letra.isalpha():
            if texto.count(letra) > 2:
                return False

    return True

def pangrama(texto):
    # Pangrama: texto que contiene todas las letras del alfabeto.
    texto = texto.lower()
    letras = "abcdefghijklmnñopqrstuvwxyz"
    for letra in letras:
        if letra not in texto:
            return False

    return True

def cleanConsole(osName):
    if osName == "nt": os.system("cls")
    else: os.system("clear")


COLOR_RESET = "\033[0m"
COLOR_CYAN = "\033[96m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"


cleanConsole(os.name)
heterogramaInput = input("Introduce la palabra para el Heterograma: ")
isogramaInput = input("Introduce la palabra para el Isograma: ")
panagramInput = input("Introduce la palabra para el Panagrama: ")

# Verificar si cada palabra es heterograma, isograma y panagrama
isHeterograma = heterograma(heterogramaInput)
isIsograma = isograma(isogramaInput)
isPanagrama = pangrama(panagramInput)
cleanConsole(os.name)


# Imprimir la tabla con los resultados
print(f"{COLOR_CYAN}+------------------+-------+--------------+{COLOR_RESET}")
print(f"{COLOR_CYAN}| TIPO DE PALABRA   | RESULTADO | PALABRA ELEGIDA {COLOR_CYAN}|{COLOR_RESET}")
print(f"{COLOR_CYAN}+------------------+-------+--------------+{COLOR_RESET}")
print(f"| Heterograma       | {COLOR_GREEN}{'Sí' if isHeterograma else 'No'}{COLOR_RESET}  | {COLOR_CYAN}{heterogramaInput}{COLOR_RESET}  |")
print(f"| Isograma          | {COLOR_GREEN}{'Sí' if isIsograma else 'No'}{COLOR_RESET}  | {COLOR_CYAN}{isogramaInput}{COLOR_RESET}  |")
print(f"| Panagrama         | {COLOR_GREEN}{'Sí' if isPanagrama else 'No'}{COLOR_RESET}  | {COLOR_CYAN}{panagramInput}{COLOR_RESET}  |")
print(f"{COLOR_CYAN}+------------------+-------+--------------+{COLOR_RESET}")