# Les bases du python / math
# Les collections. 4. Unpacking. Lists. Tuples

# 1. (~3')
# Imagine t'as une list:
l = ['Dasha', 'Chekeres', '13 ans', 'femelle', 'blonde']
# Imagine t'as une application ou t'as besoin des variables pour chaque element de la liste
# * voir exercise #4 dans matrix_007 (voir 007.4)
################################################# YOUR CODE HERE
prenom = ''
nom = ''
age = ''
sexe = ''
couleur = ''
################################################# END OF YOUR CODE
print 'mon prenom   : ', prenom
print 'mon nom      : ', nom
print 'mon age      : ', age
print 'mon sexe     : ', sexe
print 'couleur      : ', couleur

# 2. (~3' pour reflechir, rien a faire)
# Il existe une facon de faire la meme chose mais plus facilement.
# Ca s'appele "Unpacking"
# unpacking, on pourrait traduire par le terme fort moche de 'deballage',
# dans le sens 'ouvrir un colis':
p, n, a, s, c = l
print 'mon prenom   : ', p
print 'mon nom      : ', n
print 'mon age      : ', a
print 'mon sexe     : ', s
print 'couleur      : ', c
# Pour que ca marche, tu dois avoir le meme nombre des variable a gauche de '='
# que t'as des elements dans ton liste (a droite de '=')

# 3. (~15')  obligatoire, mais avec un bonus +30min d'ordi pour la solution juste
# T'as une liste des 3 listes:
les_filles = [ ['Dasha', 'Chekeres', '13ans'], ['Masha', 'Mekeres', '14ans'], ['Tasha', 'Tekeres', '12ans']]
# Cree une liste de 3 strings (chaines des characteres)
# [ 'Dasha Chekeres 13ans', 'Masha Mekeres 14ans', 'Tasha Tekeres 12ans']
# * tu dois utiliser le Unpacking
# * voir matrix_006, exercise #2 (c'est pas pareil, mais ca doit t'aider)
######################################################## YOUR CODE HERE
les_filles_str = []
######################################################## END OF YOUR CODE
print 'Les filles :', les_filles_str


# 4. - ignore cette exercise, si t'as trouver la solution de #3
# si non, essai de faire la meme chose, mais avec une liste plus facille
# t'as:
l_1 = [ ['a','x'], ['b','y'], ['c','z'] ]
# tu dois obtenir l_2 = [ 'ax', 'by', 'cz']
######################################################## YOUR CODE HERE
l_2 = []
######################################################## END OF YOUR CODE
print 'xyz = ', l_2
