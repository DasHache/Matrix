# Les bases du python / math

# Les collections. 1. Set
# Un set represents un ensemble d'objets unique, non ordonne.
# On peut cree un set avec { }
# Par examples:
s = {1, "a", "chaine des characteres", 4+5, 3-2} 
print "1. Example. Un set qui contient 4 objets: ", s

# 1.
# Trouvez que la taille de cet set,  s
s_len = 0 #rappelle d'une function qui retourne la longeur 

# 2.
# Cree un set qui contient 1,2,3,4. Sauvegarde le set dans une variable s2
s2 = {}

# 3.
# Calcule une somme de tous les object du set s2.
# Utilise la fonction sum() qui prends un set comme un argument.
s2_somme = 0

# 4.
# Cree un set s3 qui contient 0,1,2,3,4,5 en utilisant la fonction range(6)
s3 = {}

# 5.
# Imprime la list des carres des tous les membres du set s3
# comme ca:
#   s3_carres = {0*0, 1*1, 2*2, 3*3, 4*4, 5*5}
# ou comme ca:
#   s3_carres = {x*x for x in s3}
s3_carres = {}

################ YOUR CODE HERE ###############

s_len = len(s)
s2 = {1,2,3,4}
s2_somme = sum(s2)
s3 = range(6)
s3_carres = {0*0, 1*1, 2*2, 3*3, 4*4, 5*5}

############### END OF YOUR CODE ##############

print "s length   = ", s_len
print "s2         = ", s2
print "s2_somme   = ", s2_somme
print "s3         = ", s3
print "s3_carres  = ", s3_carres





