''' Ce fichier sert à créer la classe Liste '''
import json
import logging
from pathlib import Path

CUR_DIR = Path().parent.resolve()
DATA_FILE = CUR_DIR / "data" / "lists.json"
LOG_FILE = CUR_DIR / "data" / "infos.log"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=LOG_FILE,
                    filemode="a",
                    encoding="UTF-8")

# Je pense que je n'ai pas besoin de classe "item" et qu'il suffit que j'ajoute des str dans mes listes
class Liste:
    def __init__(self, name, tasks_to_do=[], tasks_done=[]):
        self.name = name
        self.tasks_to_do = []
        self.tasks_done = []

    def __str__(self):
        return self.name



    # def _get_list(self):
    #     with open(DATA_FILE, 'r') as f:
    #         return json.load(f)
    #
    # def save_list(self):
    #     current_lists_saved = self._get_list()
    #     list_to_save = {self.name : {'Undone' : self.unchecked_item_list, "Done" : self.checked_item_list}}
    #     current_lists_saved.append(list_to_save)
    #     with open(DATA_FILE, 'w') as f:
    #         json.dump(current_lists_saved, f, indent=4)
    #
    # def delete_list(self):
    #     current_lists_saved = self._get_list()
    #     # lists = {}
    #     # with open(DATA_FILE, 'r') as f:
    #     #     lists = json.load(f)
    #     current_lists_saved.pop(self.name)
    #     with open(DATA_FILE, 'w') as f:
    #         json.dump(current_lists_saved, f, indent=4)
    #
    #
    # # def select_list(self):
    # #     pass
    # #
    # # def display_list(self):
    # #     pass
    #
    # def add_item_to_list(self):
    #     pass
    #
    # def check_item(self):
    #     pass
    #
    # def uncheck_item(self):
    #     pass
    #
    # def delete_item(self):
    #     pass

if __name__ == '__main__':
    test1 = {}
    test2 = {}
    l1 = Liste("test")
    l1.checked_item_list.append("J'ai fini cette tâche")
    l1.unchecked_item_list.append("Je dois faire cette tâche")
    l1.save_list()
    with open(DATA_FILE, 'r') as f:
        test1 = json.load(f)
    l2 = Liste("test2")
    l2.checked_item_list.append("J'ai fini cette tâche2")
    l2.unchecked_item_list.append("Je dois faire cette tâche2")
    l2.save_list()
    with open(DATA_FILE, 'r') as f:
        test1 = json.load(f)
    print(test1)
    l1.delete_list()
    with open(DATA_FILE, 'r') as f:
        test2 = json.load(f)
    print(test2)