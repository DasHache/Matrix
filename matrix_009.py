# Les bases du python / math
# Les collections. 5. Les Dictionnaires

# 1.
# Le dictionnaire, comme la liste et le set, est un type de donnees 
# Le dictionnaire, comme la liste et le set, est une collection
# * rappelle: Une collection, c'est un objet qui contient d'autres objets
# * rappelle: Une collection, c'est un conteneur 
# Au meme temps, le dict. est tres different de list et set

# 1.1 (~1') rien a faire; pour se souvenir
# * rappelle: Un element d'une liste c'est un OBJET
une_liste = [1, 'a', 2.0, "string", [1,2,3]]
# element #1 c'est un entier (integer)
# element #2 c'est un charactere (char)
# element #3 c'est un ... (float)
# element #4 c'est une chaine des characteres (string)
# element #5 c'est une liste

# 1.2 (~2') rien a faire; a comprendre!
# A la difference de list, un element d'un dictionnaire
# c'est TOUJOURS une PAIRE d'objets!
une_dict = {'prenom' : 'Dasha', 'nom' : 'Chekeres', 'age' : 13 }
# element #1 c'est une paire:   'prenom' : 'Dasha'
# element #2 c'est une paire:   'nom'    : 'Chekeres'
# element #3 c'est une paire:   'age'    : 13

# 1.3 (~2') 
# Les deux objets de la paire est TOUJOURS separe par ':'
# l'objet a gauche de ':' il s'appele "une cle"    (english - key)
# l'objet a droute de ':' il s'appele "une valeur" (english - value)
# Par example, voir le dict. une_dict (defini par dessus, dans 1.2)
# la 1ere cle: 'premon', la 1ere valeur: 'Dasha'
# la 2eme cle: 'nom',    la 2eme valeur: 'Chekeres'
# En fait, c'est pas corect. On peux pas dir 1ere et 2eme parse que le dict.
# est une collection non-ordonnee,
une_autre_coll_non_ordonee_que_tu_connais_est = {'a':2,'s':'e'}# ecris 'list' ou 'set'   ### YOUR CODE HERE
print 'Non-ordonnee: ', une_autre_coll_non_ordonee_que_tu_connais_est

# 2. (~5')
# Cree un dict. et rajoute des elements
# Tu peux cree un dict. avec une fonction dict() ou {} (oui, comme un set)
mon_dict = dict()
# Tu peux rajouter un element dans un dict. avec une fonction mon_dict[ ... ] = ...
# qui prend une cle dans [ ] et une valuer apres '='
# Rajoute 2 elements dans mon_dict
# La valeur de la 1ere element est mon nom,    (la cle a ton choix)
# La valeur de la 2eme element est mon prenom, (la cle a ton choix)
mon_dict['nom'] ='Pashnin'   ### YOUR CODE HERE
mon_dict['prenom'] = 'Andrey'   ### YOUR CODE HERE
print "Mon dictionnaire: ", mon_dict
# * controle-toi: le print de la ligne precedents doit imprimer:
# Mon dictionnaire:  {'nom': 'Pashnin', 'prenom': 'Andrey'}

# 3. (~3')
# Si tu veux lire une valeur qui correspond a une cle,
# utilise juste la fonction [ ]
# Definis le deux variables suivante en utilisant mon_dict:
sensei_nom =mon_dict['nom'] ### YOUR CODE HERE
sensei_prenom = mon_dict['prenom']  ### YOUR CODE HERE
print "Mon sensei: nom = ", sensei_nom, ", prenom = ", sensei_prenom
# * controle-toi: le print de la ligne precedents doit imprimer:
# Mon sensei: nom =  Pashnin , prenom =  Andrey






