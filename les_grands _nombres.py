# En entrée on a :
# - la quantité de nombres aléatoires
# - la quantité des plus grands nombres a sélectionner parmi les nb aléatoires

# Que fait la fonction ?
# Etape 1 : générer une liste aléatoire basée sur la quantité donnée en entrée
# Etape 2 : parcourir la liste aléatoire en sélectionnant les X plus grands nombres

import random

def get_high_numbers(max_value, nb_of_values):
    # liste des nombres aléatoires
    random_list = []

    # list de résultats à sortir
    results = []

    # ETAPE 1
    # boucle pour remplir la liste des nb aléatoires
    for _ in range(max_value):
        # générer un nb aléatoire 
        x = random.randint(0, max_value)
        #puis le mettre dans la liste des nb aléatoires
        random_list.append(x)

    print(random_list)

    # ETAPE 2
        
    # tant que la taille des resultats n'a pas atteint le choix de l'utilisateur
    while len(results) < nb_of_values:
        # trouver la + grande valeur de random_list
        highest_value = max(random_list)
        # ajouter à la list results
        results.append(highest_value)
        # enlever cette valeur de la random_list
        random_list.remove(highest_value) 

    return results

print(get_high_numbers(1000, 3))