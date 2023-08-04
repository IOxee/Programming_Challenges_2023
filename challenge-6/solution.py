# Name: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK 
# Path: solution.py
# Author: IOxee
# TimeStamp: 04-08-2023 12:30:00

import random, os
playername = ""
secondplayer = "CPU"
player_choice = 0
computer_choice = 0

choices = {
    1: "✊",
    2: "🖐️",
    3: "✌️",
    4: "🦎",
    5: "🖖",
    6: "🧨"
}

rules = {
    (1, 2): "Papel cubre piedra",
    (1, 5): "Spock vaporiza piedra",
    (2, 3): "Tijera corta papel",
    (2, 4): "Lagarto devora papel",
    (3, 1): "Piedra rompe tijera",
    (3, 5): "Spock aplasta tijera",
    (4, 1): "Piedra aplasta lagarto",
    (4, 3): "Tijera decapita lagarto",
    (5, 2): "Papel desautoriza Spock",
    (5, 4): "Lagarto envenena Spock",
    (6, 1): "Piedra aplasta Dinamita",
    (6, 2): "Papel cubre Dinamita",
    (6, 3): "Tijera corta Dinamita",
    (6, 4): "Lagarto envenena Dinamita",
    (6, 5): "Spock vaporiza Dinamita",
    (6, 6): "Dinamita explota Dinamita"
}

def get_player_choice():
    while True:
        try:
            choice = int(input("Elige una opción entre 1 - 6: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Ingresa una opción válida.")
        except ValueError:
            print("Ingresa una opción válida.")
        
def get_computer_choice():
    return random.randint(1, 6)
    
def determine_winner(player_choice, computer_choice):
    if player_choice == 6 or computer_choice == 6:
        return "Dinamita"
    elif player_choice == computer_choice:
        return "Empate"
    elif (player_choice, computer_choice) in rules:
        return "Computer"
    else:
        return "Player"
    
def print_winner(winner):
    if winner == "Empate":
        print("💥 EMPATE 💥\n")
    else:
        if winner != "Dinamita":
            print(f"🔴 {playername} ha elegido {choices[player_choice]}")
            print(f"🔵 {secondplayer} ha elegido {choices[computer_choice]}")
            print(f"\n{rules[(player_choice, computer_choice)]}\n")
        else:
            print(f"\n\n\n\t🧨🧨🧨 AUTO-DESTRUCCIÓN 🧨🧨🧨")
        
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        

def generate_scoreboard(player_victories, computer_victories):
    print("⭐================================================⭐")
    print("   Piedra, Papel, Tijera, Lagarto, Spock, Dinamita!  ")
    print("⭐================================================⭐")
    print(f"🔴 {playername}: {player_victories} victorias")
    print(f"🔵 {secondplayer}: {computer_victories} victorias")
    print("⭐================================================⭐")

        
def main():
    global playername
    global secondplayer
    global player_choice
    global computer_choice
    playername = input("Ingresa tu nombre: ")
    print(f"\nHola {playername}, vamos a jugar Piedra, Papel, Tijera, Lagarto, Spock, Dinamita!")
   
    player_victories = 0
    computer_victories = 0
    mode = 0
    
    while True:
        print("⭐==============================================⭐")
        print("   Piedra, Papel, Tijera, Lagarto, Spock, Dinamita!  ")
        print("⭐==============================================⭐")
        
        # select player mode (1 or 2 players)
        if mode == 0:
            while True:
                try:
                    # menu with options
                    print("\nSelecciona el modo de juego:")
                    print("1. 1 Jugador")
                    print("2. 2 Jugadores")
                    mode = int(input("Selecciona el modo de juego (1 - 2): "))
                    if 1 <= mode <= 2:
                        break
                    else:
                        print("Ingresa una opción válida.")
                except ValueError:
                    print("Ingresa una opción válida.")
        elif mode == 1:
            clear_console()
            
            for number, emoji in choices.items():
                print(f"{number}. {emoji}")
            
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
                        
            clear_console()
        elif mode == 2:
            clear_console()
            
            for number, emoji in choices.items():
                print(f"{number}. {emoji}")
            
            player_choice = get_player_choice()
            
            if secondplayer == "CPU":
                secondplayer = input("Ingresa el nombre del segundo jugador: ")
                
            computer_choice = get_player_choice()
            
            
            clear_console()
        else:
            continue
        
        if player_choice == 0 and computer_choice == 0:
            continue
        
        winner = determine_winner(player_choice, computer_choice)
        
        print_winner(winner)
            
        if winner == "Player":
            player_victories += 1
            print(f"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n  {playername} ha ganado! 🥳\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n\n")
        elif winner == "Computer":
            computer_victories += 1
            print(f"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n  {secondplayer} ha ganado! 🥳\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n\n")
        elif winner == "Dinamita":
            print(f"\n\n\n\t🧨🧨🧨 AUTO-DESTRUCCIÓN 🧨🧨🧨")
            
            
        repeat = input("¿Quieres jugar de nuevo? (s/n): ")
        if repeat.lower() == "n":
            mode = 0
            clear_console()
            generate_scoreboard(player_victories, computer_victories)
            break
        
    
if __name__ == "__main__":   
    playername = ""
    secondplayer = "CPU"
    player_choice = 0
    computer_choice = 0 
    
    main()