import requests
from tabulate import tabulate
import os

def clear_console():
    if os.name == "unix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_last_commits(repo_url, count=10):
    commits_url = f"{repo_url}/commits"
    response = requests.get(commits_url)

    if response.status_code == 200:
        commits_data = response.json()
        last_commits = commits_data[:count]

        table_data = []
        commit_id = 0
        for commit in last_commits:
            commit_id = commit_id + 1
            sha = commit['sha']
            author = commit['commit']['author']['name']
            date = commit['commit']['author']['date']
            message = commit['commit']['message']

            table_data.append([commit_id, sha, author, date, message])

        headers = ['ID', 'SHA', 'Autor', 'Fecha', 'Mensaje']
        table = tabulate(table_data, headers=headers, tablefmt='grid')

        clear_console()
        print("\n")
        print(table)
        print("\n")
    else:
        print("Error al obtener los commits.")
        
        
if __name__ == "__main__":
    input_user = input("Introduce el usuario: ")
    input_repo_name = input("Introduce el nombre del repositorio: ")
    repo_url = f"https://api.github.com/repos/{input_user}/{input_repo_name}"
    #repo_url = "https://api.github.com/repos/IOxee/IOxee"  # Reemplaza "usuario/repo" por la ruta a tu repositorio
    get_last_commits(repo_url)
