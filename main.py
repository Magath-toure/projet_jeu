 
#------- Import des class ----------
from class_jeu import Hero, Monstre

#------- Instanciation des class ---------

troll = Monstre("troll", 5, 1, 1)
robin_des_bois = Hero("Robin des bois", 10, 3)

# ------ Structure du jeu avec une boucle while --------

départ_jeu = input("Voulez-vous commencer / recommencer ? Tapez 'oui' ou 'non': ")

if départ_jeu == "oui":
    # on donne une indication à l'utilisateur quel personnage il incarne et de combien de PV il dispose.
    print(f"Vous incarnez {robin_des_bois.nom} - {robin_des_bois.nombre_point_de_vie} PV - {robin_des_bois.nombre_potions} potion(s)")

    while troll.nombre_point_de_vie > 0 and robin_des_bois.nombre_point_de_vie > 0: # tant que le monstre ou le hero a encore de la vie, le jeu continue.
        print(f"\n Vous rencontrez le {troll.name} - {troll.nombre_point_de_vie} PV - {troll.degat_attaque} d'attaque ")
        robin_des_bois.choix_action(troll)

        if troll.nombre_point_de_vie > 0:
            troll.attaque_hero(robin_des_bois)
        else:
            # diadème --- 
            print("Vous avez gagné")
        
# le hero rencontre un monstre, il doit choisir d'attaquer ou de se soigner
        










