# Les bases du python / math
# Les collections. 7. Comprehension

# 1. (~10')
# Qu'est-ce que c'est La Comprehension? 
# Tu l'utilise deja depuis qq jours.
# C'est une expression sous la forme de [ ... for ... in ... ]
# qui produit une liste, un set ou un dict
# 
# Essai le code suivant et trouve la difference entre
# la comprehension de liste, set et dict
ll = [ ['a', 0],  ['b', 1],  ['c', 2],  ['d', 3] ]
comprehension_list = [ x * y  for x,y in ll]  # ligne 1.1 
comprehension_set  = { x * y  for x,y in ll}  # ligne 1.2
comprehension_dict = { x : y  for x,y in ll}  # ligne 1.3
print '--------------------------------------------------'
print 'list = ', comprehension_list
print 'set  = ', comprehension_set 
print 'dict = ', comprehension_dict
print '--------------------------------------------------'

# Reponds sur chaque question avec 2 mots (pas plus):
# - quelle est la difference entre la ligne 1.1 et la ligne 1.2 ?
print 'Diff entre [x*y for x,y in ll] et {x*y for x,y in ll} est = ', 'TON EXPLICATION ICI'
# - pourquoi la ligne 1.2 produit un set, mais 1.3 produit une liste ? 
print 'Parse que ', 'TON EXPLICATION ICI'
# - quelle est la difference entre la ligne 1.2 et la ligne 1.3 ?
print 'Diff entre {x*y for x,y in ll} et {x*y for x,y in ll} est = ', 'TON EXPLICATION ICI'
# - pourquoi la ligne 1.3 produit un dict ? (tant que la ligne 1.2 produit un set) 
print 'Parse que ', 'TON EXPLICATION ICI'


# 2. (~7')
# Essai le code suivant et trouve la difference entre l'exercise #1
lx = ['a', 'b', 'c', 'd'] 
ly = [ 0 ,  1 ,  2 ,  3 ]
comprehension_list = [ x * y  for x in lx for y in ly]  # ligne 2.1
comprehension_set  = { x * y  for x in lx for y in ly}  # ligne 2.2
comprehension_dict = { x : y  for x in lx for y in ly}  # ligne 3.3
print '--------------------------------------------------'
print 'list = ', comprehension_list
print 'set  = ', comprehension_set 
print 'dict = ', comprehension_dict
print '--------------------------------------------------'
# A reflechir:
# - quelle est la difference entre la ligne 1.1 et la ligne 2.1 ?
print 'Diff entre [x*y for x,y in ll] et [x*y for x in lx for y in ly] est = ', 'TON EXPLICATION ICI'


# 3. (~5')
# Cree un dict les cles duquel sont les chiffres de 0 a 9,
# et les valeurs sont les carrees de chiffres de 0 a 9
# c'est a dire: {0:0, 1:1, 2:4, 3:9, ...}
# * utilise le comprehension
# * utilise la fonction range(10)
# * tu dois comprendre que une cle d'un dict peux etre un entier (une chiffre)
#   le cle ce n'est PAS TOUJOURS une chaine des characteres (a string)
dict_carrees = 
print 'Dictionnaire des carrees: ', dict_carrees











