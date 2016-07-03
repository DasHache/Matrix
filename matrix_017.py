# 2016.06.02
# Les bases du Python, programming.
# Les classes - 2.

# Voir 'TON CODE ICI' plus bas, c'est la ou tu dois ecrire tous le code

# 1.
# Cree une classe (nom: 'Animal') pour les animaux.
# Trois ligne de code, juste ce qui est necessaire.
# * voir matrix_016.py
# Verifie si tout va bien. Cree une variable du type Animal. Imprime-la avec print.

# 2.
# Modifie ta classe: Rajoute un attribut qui s'appele 'nom'
# * voir matrix_016.py
# Verifie si tout va bien. Cree une variable du type Animal. Imprime-la avec print.

# 3.
# Modifie ta classe: Rajoute une fonction qui change
# comment un objet (une variable) de ta classe s'imprime.
# * voir matrix_016.py
# Verifie si tout va bien. Cree une variable 'a' du type Animal. Imprime-la avec print.
# Corrige la classe pour que 'print a' imprime une phrase "JE NE SAIS PAS MON NOM"

# 4.
# Modifie ta classe: Rajoute une fonction qui s'appele 'parle'
# qui n'a pas d'argument (sauf 'self') et
# qui retourne une phrase 'JE NE SAIS PAS CE QUE JE PARLE'

# 5. 
# Verifie si tout va bien. Cree un objet 'a' (une variable) du type Animal.
# Appele la methode (la fonction) 'parle' de cet objet
# * rappele: on appele une methode d'un objet en utilisant '.'
#            comme ca: objet.methode()
# Ca doit imprimer la phrase 'JE NE SAIS PAS CE QUE JE PARLE'

############################################# TON CODE ICI #############


class Animal :

    def __init__(self):
        self.nom = "JE NE SAIS PAS MON NOM"

    def __str__(self):
        return  self.nom
        
    def parle(self):
        return 'JE NE SAIS PAS CE QUE JE DIS'

a = Animal()
print a
print a.parle()


class Cat(Animal) :
    def __init__(self):
        self.nom = "un chat"

    def parle(self):
        return 'miaou miaou'

class Dog(Animal) :
    def __init__(self):
        self.nom = "un chien"

    def parle(self):
        return 'gggg'



c = Cat()
print c
print c.parle()

d = Dog()
print d.parle()
########################################################################
