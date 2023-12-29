
#------- Import des class ----------
from class_jeu import Hero, Monstre
import random

#------- Instanciation des class ---------

troll_1 = Monstre("troll 1", 5, 1)
troll_2 = Monstre("troll 2", 5, 2)
troll_3 = Monstre("troll 3", 5, 3)
liste_monstre = [troll_1, troll_2, troll_3]

robin_des_bois = Hero("Robin des bois", 10, 3)

# ------ Structure du jeu avec une boucle while --------
game_continue = True
départ_jeu = input("Voulez-vous commencer / recommencer ? Tapez 'oui' ou 'non': ")

if départ_jeu == "oui": 
     
        for monstre in liste_monstre:
            if game_continue == False:
                print("Vous êtes décédé")
                break
            # on donne une indication à l'utilisateur quel personnage il incarne et de combien de PV il dispose.
            print(f"Vous incarnez {robin_des_bois.nom} - {robin_des_bois.nombre_point_de_vie} PV - {robin_des_bois.nombre_potions} potion(s)")
            print(f"\n Vous rencontrez le {monstre.name} de niveau {monstre.niveau} - {monstre.nombre_point_de_vie} PV ")
            while monstre.nombre_point_de_vie > 0 and robin_des_bois.nombre_point_de_vie > 0: # tant que le monstre ou le hero a encore de la vie, le jeu continue.
                
                if robin_des_bois.nombre_point_de_vie > 0:
                    robin_des_bois.choix_action(monstre)
                    

                if monstre.nombre_point_de_vie > 0:
                    monstre.attaque_hero(robin_des_bois)
                    if robin_des_bois.nombre_point_de_vie <= 0:
                        game_continue = False
                        break
                else:
                    # diadème --- 
                    print("Vous avez gagné")
                    
            # le hero rencontre un monstre, il doit choisir d'attaquer ou de se soigner
                










