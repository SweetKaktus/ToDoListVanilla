''' Ce fichier sert à créer la classe Liste '''

# Je pense que je n'ai pas besoin de classe "item" et qu'il suffit que j'ajoute des str dans mes listes
class Liste:
    def __init__(self, name):
        self.name = name
        self.checked_item_list = [str]
        self.unchecked_item_list = [str]

    def create_liste(self):
        ''' Cette fonction doit servir à créer une liste et à la stocker
        dans le json /data/lists.json. Elle doit contenir une liste d'item check, et une liste d'item unchecked '''
        pass

    def create_item(self):
        pass