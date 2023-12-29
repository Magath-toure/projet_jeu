class Hero:

    def __init__(self, nom, nombre_point_de_vie, nombre_potions):
        self.nom = nom
        self.nombre_point_de_vie = nombre_point_de_vie
        self.nombre_potions = nombre_potions

    def choix_action(self):
        pass

    def attaquer_monstres(self):
        pass

    def utiliser_potion(self):
        pass

    def diademe_recupere(self):
        pass

class Monstre:
    
    def __init__(self, name: str, nombre_poin_de_vie: int, niveau : int, degat_attaque: int):
        
        self.name = name
        self.nombre_poin_de_vie = nombre_poin_de_vie
        self.niveau = niveau
        self.degat_attaque = degat_attaque
    def attaquer_hero(self):
        print("il peut attaquer le monstre")
    def mort_du_montre(self):
        print("il peut tuer le monstre")
    
