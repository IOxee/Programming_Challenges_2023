# Name: La Trifuerza 
# Path: solution.py
# Author: IOxee
# TimeStamp: 04-08-2023 13:32:12

def print_spaces(number: int):
    for j in range(number):
        print("",end=' ')


def print_asterisks(number: int):
    for k in range(number):
        print("\033[33m*\033[0m", end=" ")


def print_Power(size: int, lastRowSize: int):
    for i in range(size):
        print_spaces(lastRowSize-i)
        print_asterisks(i+1)
        print_spaces(lastRowSize-i)
        print(" ")


def print_Wisdom_and_Courage(numberOfRows: int, lastRowSize: int):
    for i in range(numberOfRows):
        print_spaces((numberOfRows-i)-1)
        print_asterisks(i+1)
        print_spaces((lastRowSize-(2*i)-1))
        print_asterisks(i+1)
        print_spaces((numberOfRows-i)-1)
        print(" ")


def print_Triforce(numberOfRows: int, lastRowSize: int):
    print_Power(numberOfRows, lastRowSize)
    print_Wisdom_and_Courage(numberOfRows, lastRowSize)
    print(" ")


def what_size() -> int:
    size = False
    print("¿Qué tan grande quieres tu triforce?:")
    while size == False:
        try:
            number = int(input(" "))
            print(" ")    
            if number > 0 and type(number) == int:
                size = True
                print("")
            else:
                print("¡Por favor! Escribe un número entero positivo:")
        except ValueError:
            print("¡Por favor! Escribe un número entero positivo:")
    print("")
    return number

def print_end():
    print("""
    ⢦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤
    ⠘⣿⣿⣿⣷⣦⣄⣀⠀⢠⠔⠀⢀⡼⠿⠿⢆⠀⠀⠲⣄⠀⣀⣠⣴⣾⣿⣿⣿⠇
    ⠀⠈⠉⠉⠛⠛⠻⠿⢿⣿⠀⢀⣾⣷⡀⢀⣾⣷⡀⠀⣿⡿⠿⠿⠛⠛⠉⠉⠁⠀
    ⠀⠀⣤⣤⣶⣶⣶⣶⣶⣿⣆⠈⠉⠉⠉⠉⠉⠉⠉⢠⣿⣶⣶⣶⣶⣶⣤⣤⠀⠀
    ⠀⠀⠘⣿⡿⠟⠛⠉⣡⣿⣿⣷⣤⠀⢠⣆⠀⣤⣶⣿⣿⣬⡉⠛⠻⠿⣿⠇⠀⠀
    ⠀⠀⠀⠀⠀⢀⣴⣿⡿⢋⣿⣿⠛⢠⣿⣿⡄⠛⢿⣿⡘⢿⣿⣦⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠻⠏⠀⣸⣿⡇⢀⠻⣿⣿⠟⣀⠸⣿⣇⠀⠙⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⡟⠁⣿⣿⠀⠻⣆⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢟⠉⠙⠓⠀⠘⠏⠀⠘⠟⠉⡻⠋⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("")
    print("Take care of Hyrule!")
    print("")


def main():
    """Allows the user to print one or more Triforce."""
    finish = False

    while finish == False:
        finish2 = input("¿Quieres imprimir una trifuerza? (s/n): ")
        sizeTriforce = what_size()
        print_Triforce(sizeTriforce, sizeTriforce*2-1)
        if finish2 == "s":
            finish = True
            continue
        
    print_end()



if __name__ == "__main__":
    main()
