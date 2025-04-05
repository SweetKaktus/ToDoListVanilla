''' Ce fichier me sert à créer la classe item '''

# Cette classe est-elle vraiment utile ? Ne ferais-je pas mieux de gérer mes listes uniquement avec des str?
# Cette classe item me servira quand je ferai une app plus complexe avec la gestion d'inforamtions (genre liste de course avec prix, rayon, etc.)
class Item:
    def __init__(self, name: str):
        self.name = name
        self.is_checked = False

    #Ai-je vrm besoin de ce paramètre et cette fonction ? Ne serait-ce pas mieux de gérer directement depuis la classe Liste ?
    def check_item(self):
        self.is_checked = True

    def uncheck_item(self):
        self.is_checked = False