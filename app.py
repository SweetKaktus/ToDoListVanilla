''' Ce fichier gère le fonctionnement de l'app '''
import json
from pathlib import Path
from liste import Liste

CUR_DIR = Path().parent.resolve()
DATA_FILE = CUR_DIR / "data" / "lists.json"


lists_registered = []
lists_to_save_in_json = {}

def get_lists_registered():
    with open(DATA_FILE, 'r') as f:
        lists_to_save_in_json = json.load(f)
    if not lists_to_save_in_json:
        print('Pas de liste enregistrée')
    else:
        for key, value in lists_to_save_in_json.items():
            lists_registered.append(Liste(name=key, tasks_to_do=value['TO DO'], tasks_done=value['DONE']))

def save_lists():
    for element in lists_registered:
        lists_to_save_in_json.update({element.name : {'TO DO' : element.tasks_to_do, 'DONE' : element.tasks_done}})
        print(lists_to_save_in_json)
    with open(DATA_FILE, 'a') as f:
        json.dump(lists_to_save_in_json, f, indent=4)

def create_liste(name):
    lists_registered.append(Liste(name))

def select_screen(lists_registered):
    print('Lists:')
    for index, element in enumerate(lists_registered):
        print(f'{index}. {element}\r')

    print('Choisissez une action:\r')
    print('1. Selectionner une liste\r2. Creer une liste\r3. Supprimer une liste')
    manage_input_list_selection()

def manage_input_list_selection():
    choix = input('Action: ')
    match choix:
        case '1':
            print('Selectionner liste')
        case '2':
            list_name = input('Choisissez un nom pour votre liste')
            create_liste(list_name)
            save_lists()
            print_app_title()
            select_screen(lists_registered)
        case '3':
            print('Supprimer liste')
        case _:
            print("Votre choix est incorrect, veuillez recommencer")
            select_screen(lists_registered)

def print_app_title():
    print('=' * 11)
    print('TO DO')
    print('=' * 11)

def select_list():
    pass


if __name__ == '__main__':
    create_liste(name='Taches du jour')
    create_liste(name='Taches pro')
    lists_registered[0].tasks_to_do.append('Manger un croissant')
    lists_registered[0].tasks_to_do.append('Passer le balai')
    lists_registered[0].tasks_done.append('Acheter des yaourts')
    lists_registered[0].tasks_done.append('Faire la vaisselle')
    lists_registered[1].tasks_to_do.append('traiter alertes')
    lists_registered[1].tasks_to_do.append('traiter tickets')
    lists_registered[1].tasks_done.append('comm client')
    lists_registered[1].tasks_done.append('factu')
    save_lists()
    print_app_title()
    select_screen(lists_registered)