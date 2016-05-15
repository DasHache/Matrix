# Les bases du python / math

# Les collections. 3. List
# Une liste represent un ensemble d'objets NON-unique, MAIS ordonne.
# On cree une liste: [...] ou list(...)
print "Une example d'une list: ", [1,1,1,3-2,'a']
print "En utilisant un set   : ", list(  {1,2,3} )
print "En utilisant range()  : ", list( range(10) )
# !! c'est une erreur        :    list( 1,2,3 )   

# 1. (le temps estimee ~2')
# C'est possible d'avoir une liste des listes!
print "Une liste des liste   : ", [ [1,2,3,4], ['a','b','c','d'] ]
# Tu NE PEUX PAS faire pareil avec les sets, essai la suivante:
# { {1,2,3}, {'a','b','c'} }
# Cree une liste qui contient 3 listes (a ton choix):
liste_a_ton_choix = []  # <------------------------------- YOUR CODE HERE
print '\n*** 1. Une liste des listes: ', liste_a_ton_choix

# 2. (~2')
# Les fonctions comme 'len' et 'sum' marchent aussi:
# Trouve la longeur de la liste l1 et la somme des elements
l1 = [1,2,3,4,5]
l_len = 0 # <------------------------------- YOUR CODE HERE
l_som = 0  # <------------------------------- YOUR CODE HERE
print '\n*** 2.1 La longeur: ', l_len
print '\n*** 2.2 La somme:   ', l_som

# 3. (~2')
# Tu peux rajouter les listes avec +
l2 = [1,2,3,4]
l3 = [10,20,30,40]
# Cree une liste qui contient tous les elements des l2 et l3
l2_plus_l3 = []  # <------------------------------- YOUR CODE HERE
print '\n*** 3. Une somme de deux listes: ', l2_plus_l3

# 4. (~10')
print '\n*** 4. Les indices'
# A la difference de set, avec les listes on peut prendre l'element par son index:
l_15 = list( range(15) )
print l_15[1],    ' - est le deuxieme element de la liste'
a = 5
b = 9
# Essai le code et remplace les dots par tes explications
print l_15[a],    ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[a:b],  ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[:b],   ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[b:],   ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[::3],  ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[::3],  ' - est ...............................' # <------------------------------- YOUR CODE HERE
print l_15[a:b:2],' - est ...............................' # <------------------------------- YOUR CODE HERE



# 5. Pas obligatoire. Si tu trouve une solution: +3 heurs d'ordinateur supplementaires

# En utilisant les liste d'exercise #3 - l2 et l3
# cree une nouvelle liste chaque element duquelle est une somme
# des elements correspondants des list l2 et l3
# C'est a dire, tu dois construire la liste [11, 22, 33, 44] ou 11 = 1+10, 22=2+20, ...
# 
# * Ca peut t'aider:
# * le truc que t'as fait avec les sets dans matrix_006, exercise 4.
# * le fait que 1  est l2[0],  2 est l2[1],  3 est l2[2], ...
# * le fait que 10 est l3[0], 20 est l3[2], 30 est l3[2], ...
# * le fait que l2[i] = 1 et l3[i] = 10  quand i = 0
# * rappelle que tu peut construire une list [0,1,2,3] avec: range( len(l2) )
l_somme_l2l3 = [] # <------------------------------ YOUR CODE HERE
print '\n!5. La liste des sommes: ', l_somme_l2l3
