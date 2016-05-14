# Les bases du python / math

# Les collections. 2. Encore plus des Sets
# Un set represents un ensemble d'objets unique, non ordonne.

# 1.
# Il s'arrive que t'as pas toujours besoin de tous les elements d'un set.
# Comment peut-on construir un set de tous les nombres pairs inferieur a 20?
s = set(range(20)) # un set de tous le nombre inferieur a 20
# L'expression suivante genere le meme set:
s2 = {x for x in s}
# Utilise un truc qui s'appele "un filtre":
s3 = {x for x in s if (x%2 == 0)}
# Maintenant, tu peux cree un set de tous les nombres impairs de s
# * utilise le set s ou s2
# * utilise un operateur "non egal" que t'as appris dans matrix_004
s_impairs = {}

# 2.
# Qu'est ce qui s'passe ici?:
s_xy = {x+y for x in {2,3,4} for y in {10,20,30}}
# Si ce n'est pas claire, utilise le "Python console" pour jouer avec
# Tu peux essayer les valeurs differents: {x+y for x in {1,2,3} for y in {4,5}}
# -
# Cree un set qui contient tous les combinaisons des 2 lettres
# la premier lettre vient du set {a,b,c}
# la deuxieme lettre vient du set {x,y,z}
# Tu dois avoir quelque chose comme ca: ('ax', 'ay', 'bx', ..)
# * rappelle: python ne comprends pas des lettres, que des characteres: 'a', 'b'...
# * rappelle: tu peux rajouter 2 characteres: 'a'+'b' = 'ab'
s_abcxyz = {}

# 3.
# Cree un set qui contient toutes les multiplications x * y
# ou:
#  x est un nombre de set {1,2,3,4}
#  y est un nombre de set {5,6,7}
s_mult_xy = {}

# 4.
# En utilisant le set precedant - s_mult_xy,
# cree un set qui contien tous les valeur de set s_mult_xy,
# qui sont plus petit que ou egal a 15
# * l'indice: {................ if x*y ... 15}
s_mult_xy_lt15 = {}

################ YOUR CODE HERE ###############

s_impairs = {}
s_abcxyz = {}
s_mult_xy = {}
s_mult_xy_lt15 = {}

############### END OF YOUR CODE ##############

print "Les nombres impairs <20      = ", s_impairs
print "Les permutation abc & xyz    = ", s_abcxyz
print "Les multiplication 1234, 567 = ", s_mult_xy
print "          ... inferieux a 15 = ", s_mult_xy_lt15





