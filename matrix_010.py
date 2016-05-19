# Les bases du python / math
# Les collections. 6. Les Dictionnaires - 2

# 1.
# Cree un dict. (il doit contenir au moins 2 paires de   'cle' : valeur)
# Je veux que ca soit un dict. des acteurs et roles d'un spectacle que vous jouer au theatre
# comme ca: dasha joue joulette, pasha joue romeo, sasha joue une vase de fleurs
# mets le dans une variable rj (pour Romeo & Juliet)
rj = {'juliette':'dasha',"romeo":"mitya ","joue rien": "olivier","romeo":" danya" }  ## <---------------------------------------------------------------- "YOUR CODE HERE"

# 2.
# Rajoute encore un element dans ton_dict
rj['juliette'] =' sophie'  ## <--------------------------------------------------------------------------- "YOUR CODE HERE"
print 'Acteurs principaux: ', rj

# 3.
# Maintenant, cree un dict de remplacants pour chaque role (au cas ou l'acteur principal tombe malade)
rj_remp = {'juliette':' dasha2',"romeo":"??","rien": " personne","romeo":" ???" }    ## <--------------------------------------------------------------------------- "YOUR CODE HERE"
print 'Acteurs remplacants: ', rj_remp

# 4. 
# Ca devient plus complique...
# Cree un troisieme dict qui contient le deux dict precedents - comme les valeur
# et les cles sont a ton choix
d_cast={"key":rj,"tic":rj_remp}   ## <------------------------------------------------- "YOUR CODE HERE"
print 'Les deux trouppes: ', d_cast

# 5. 
# En utilisant le dict rj, imprime le nom d'acteur qui joue un role de Romeo
acteur_romeo = rj["romeo"]## <----------------------------------------------------------------------- "YOUR CODE HERE"
print 'Romeo est: ', acteur_romeo

# 6.
# En utilisant le dict d_cast, imprime le nom du remplacant pour le role de Juliet
acteur_juliet = rj_remp['juliette'] ## <----------------------------------------------------- "YOUR CODE HERE"
print 'Deuxieme Juliet est: ', acteur_juliet

# 7.
# Imagine que la famille d'un des acteurs principale vient de demenager
# et vous avez trouve un autre garcon pour ce role
# Corrige le dict d_cast pour qu'il soit juste
d_cast['romeo']='lol'  ## <--------------------------------------------------------------------------- "YOUR CODE HERE"
print 'Le nouveau trouppe est: ', d_cast





