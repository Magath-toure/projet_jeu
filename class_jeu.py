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
            print("\nVous attaquez le monstre")
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
            print(f"\nLe monstre a {monstre_attaqué.nombre_point_de_vie} points de vie")
            # monstre_attaqué.attaque_hero(self)
        else:
            print("Le monstre est mort")
            
                

    def utiliser_potion(self):
        self.nombre_point_de_vie += 1
        self.nombre_potions -= 1
        print(f"\nIl vous reste {self.nombre_potions} potions et vous avez {self.nombre_point_de_vie} PV")
        

    def diademe_recupere(self):
        pass


class Monstre:
    
    def __init__(self, name: str, nombre_point_de_vie: int, niveau : int, degat_attaque: int):
        
        self.name = name
        self.nombre_point_de_vie = nombre_point_de_vie
        self.niveau = niveau
        self.degat_attaque = degat_attaque

    def attaque_hero(self, hero_attaqué):

        if isinstance(hero_attaqué, Hero):
            hero_attaqué.nombre_point_de_vie -= self.degat_attaque
            print(f"\nLe monstre vous a attaqué et il vous reste {hero_attaqué.nombre_point_de_vie} PV")
            
        # hero_attaqué.choix_action(self)