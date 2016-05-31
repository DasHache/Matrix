# Les bases du python / math
# Les collections. 9. Rappelle 2


# 1. 
# T'as une liste:
une_liste = ['a', 'b', 'c']
# En utilisant cette liste cree une autre liste qui contient
# toutes les paires (les permutations, voir le Wikipedia) possibles
# de facon que:
#   le premier element du paire vient de 'une_liste'
#   la dexieme element du paire et une des chiffres 0, 1, 2
# * rappelle: la fonction range(3)
# * une paire peut etre une liste ou une set (a ton choix)
# * ton liste va contenir 9 paires
l_9paires = [ [x,y] for x in une_liste for y in range(3)]


# 2. 
# En utilisant le meme liste 'une_liste'
# cree une autre liste qui contient juste trois paires:
# [ ('a', 0), ('b', 1), ('c', 2) ]
l2 = range(3)
l_3paires = [  [une_liste[x],l2[x] ]   for x in range(3)]

# 3.
# Cree un dictionnaire de 3 elements:
#  les cles:    les elements de 'une_liste'
#  les valeurs: les elements de l_3paires
d_3elem = { une_liste[x]:l_3paires[x] for x in range(3)}

# 4.
# Une nouvelle chose: Zip
# Zip c'est une fonction de Python
# Elle permet de combiner plusieurs listes en une seule
# Par example:
# x = [1,  2,  3]
# y = [10, 20, 30]
# zip(x, y) ----> va generer une liste: [(1, 10), (2, 20), (3, 30)]
# (essai dans Python Console)
#
# Essai de faire l'exercise #2 avec la fonction 'zip'
# c'est a dire:
# * tu ne utilise pas Le Comprehension
# * tu utilise zip()
# * tu utilise range()
l_3paires_zip = [zip(une_liste,l_3paires)]
range(3)





