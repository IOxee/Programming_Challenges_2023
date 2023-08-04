import os, datetime

def create_challenge_folder():
    num = input("Ingresa un número para crear la carpeta: ")
    try:
        num = int(num)
    except ValueError:
        print("Error: Ingresa un número válido.")
        return

    folder_name = f"challenge-{num}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        challenge_name = input("Ingresa el nombre del reto: ")
        with open(os.path.join(folder_name, "solution.py"), 'w') as file:
            file.write(f"# Name: {challenge_name} \n# Path: solution.py\n# Author: IOxee\n# TimeStamp: " + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + "\n\n")
            pass
        
        with open(os.path.join(folder_name, "description.md"), 'w') as file:
            file.write(f"<center><h1>{challenge_name}</h1></center>")
            pass
        
        print(f"Carpeta '{folder_name}' creada con éxito.")
    else:
        print(f"La carpeta '{folder_name}' ya existe.")

if __name__ == "__main__":
    create_challenge_folder()
