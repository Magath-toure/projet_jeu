import random

class Hero:

    def __init__(self, nom, nombre_point_de_vie, nombre_potions=3, degats=1):

        self.nom = nom
        self.nombre_point_de_vie = nombre_point_de_vie
        self.nombre_potions = nombre_potions
        self.degats = degats

    def choix_action(self, monstre_attaqué): 
        # cette méthode va permettre de choisir entre la méthode "attaquer" ou la méthode "utiliser une potion"
        
        choix = input(f"\nvoulez-vous attaquer (choix 1) ou vous soigner (choix 2): ")
        if choix == "1":
            print(f"\nVous attaquez {monstre_attaqué.name}")
            self.attaquer_monstre(monstre_attaqué)
        elif choix == "2":
            print("\nVous utilisez une potion")
            self.utiliser_potion()
        else:
            print("\nVous devez tapez 1 ou 2")
            self.choix_action(monstre_attaqué)

    def attaquer_monstre(self, monstre_attaqué):
            
        monstre_attaqué.nombre_point_de_vie -= self.degats

        if monstre_attaqué.nombre_point_de_vie > 0:
            print(f"\n{monstre_attaqué.name} - {monstre_attaqué.nombre_point_de_vie} PV")
            # monstre_attaqué.attaque_hero(self)
        else:
            print(f"Le {monstre_attaqué.name} est mort")
            
                

    def utiliser_potion(self):
        self.nombre_point_de_vie += 2
        self.nombre_potions -= 1
        print(f"\n Vous récupérez de la vie - {self.nombre_point_de_vie} PV - {self.nombre_potions} potion(s)")
        

    def diademe_recupere(self):
        pass


class Monstre:
    
    def __init__(self, name: str, nombre_point_de_vie: int, niveau : int):
        
        self.name = name
        self.nombre_point_de_vie = nombre_point_de_vie
        self.niveau = niveau

    def attaque_hero(self, hero_attaqué):

        if isinstance(hero_attaqué, Hero):
            hero_attaqué.nombre_point_de_vie -= random.randint(1, self.niveau*2)
            print(f"\nLe {self.name} vous a attaqué et il vous reste {hero_attaqué.nombre_point_de_vie} PV")
            
        # hero_attaqué.choix_action(self)