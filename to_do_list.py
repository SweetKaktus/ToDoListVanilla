import json
import sys
from pathlib import Path

CUR_DIR = Path().parent.resolve()
DATA_FILE = CUR_DIR / "data" / "lists.json"

whole_lists = [[],[]]

def load_lists() -> list[list[str],list[str]]:
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def delete_task(task_index: int) -> None:
    for index, task in enumerate(whole_lists[1]):
        if task_index == index:
            whole_lists[1].remove(task)
            print(f'La tache {task} a ete supprimee.')


def add_task(task_name: str) -> None:
    whole_lists[0].append(task_name)
    print(f'La tache {task_name} a ete ajoutee avec succes !')

def check_task(task_index: int) -> None:
    for index, task in enumerate(whole_lists[0]):
        if task_index == index:
            whole_lists[0].remove(task)
            whole_lists[1].append(task)
            print(f'La tache {task} a ete cochee.')

def uncheck_task(task_index: int) -> None:
    for index, task in enumerate(whole_lists[1]):
        if task_index == index:
            whole_lists[1].remove(task)
            whole_lists[0].append(task)
            print(f'La tache {task} a ete decochee.')

def save_lists() -> None:
    with open(DATA_FILE, 'w') as f:
        json.dump(whole_lists, f, indent=4, ensure_ascii=False)
    print('Les donnees ont ete sauvegardees.')

def delete_all_tasks() -> list[list[None]]:
    global whole_lists
    whole_lists = [[],[]]

def display_ui() -> None:
    print('=' * 11)
    print('TO DO LIST')
    print('=' * 11)
    print('\r')

    print('TO DO :')
    print('\r')
    for index, task in enumerate(whole_lists[0]):
        print(f"{index}. [] {task}")

    print('\r')
    print('DONE :')
    print('\r')

    for index, task in enumerate(whole_lists[1]):
        print(f"{index}. [X] {task}")

    print('\r')
    print('Actions:')
    print('\r')
    print('''1. Ajouter une tache
2. Supprimer une tache
3.Cocher une tache
4. Decocher une tache
5. Sauvegarder les données
6. Supprimer toutes les taches
7. Quitter application''')
    user_choice()

### Les 2 fonctions ci-dessous peuvent être amenées à changer si trop complexes à construire ###
def user_choice() -> list[str]:
    test = False
    while not test:
        try:
            users_choice = int(input('Que souhaitez-vous faire ? '))
        except ValueError:
            print('Veuillez saisir un nombre valide')
        else:
            match users_choice:
                case 1:
                    test = True
                    task_name = input('Veuillez saisir le nom de la tache a ajouter: ')
                    add_task(task_name)
                    display_ui()
                case 2:
                    test = True
                    task_index = int(input('Veuillez saisir le numero de la tache cochee a supprimer: '))
                    delete_task(task_index)
                    display_ui()
                case 3:
                    test = True
                    task_index = int(input('Veuillez saisir le numero de la tache a cocher: '))
                    check_task(task_index)
                    display_ui()
                case 4:
                    test = True
                    task_index = int(input('Veuillez saisir le numero de la tache a cocher: '))
                    uncheck_task(task_index)
                    display_ui()
                case 5:
                    test = True
                    save_lists()
                    display_ui()
                case 6:
                    test = True
                    delete_all_tasks()
                    print('Toutes les taches ont ete supprimees.')
                    display_ui()
                case 7:
                    sys.exit()
                case _:
                    print('Veuillez saisir un numero valide')

if __name__ == '__main__':
    whole_lists = load_lists()
    display_ui()