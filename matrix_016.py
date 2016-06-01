# 2016.06.01
# Les bases du python / math
# Les classes.

# Qu'est ce que c'est une classe?
# - C'est un type de donne
# Quelle-est la difference entre le type de donnee 'chaine des characteres'
# et une class? 
# - Une class c'est un type que tu definis toi meme!
# Pourquoi veux-tu definir un type? 
# - Parse que tu n'as toujour pas un type dont t'as besoin! 
# 
# Par example, t'as un type de donnee 'List' ou 'Dictionary',
# mais, tu n'as pas un type de donnee 'Emotion'
# C'est pas tres pratique si on veux creer une application
# qui gere les emotions humaine.
# 
# On va creer une classe Emotion,
# qui va servir comme un type de donnee 'une emotion'.

# 1.
# On definit une classe avec un mot 'class' suivi par le nom:
# Chaque classe doit avoir une fonction qui s'appele '__init__(self)'
class Emotion:
    def __init__(self):
        pass
# Le mot 'pass' sert comme le corps de la fonction
# (ca te donne une fonction qui fair rien)

# Voila, ton premier type de donnee est pret.
# Oui, il fait rien. Il n'est pas tres pratique. Mais, c'est le debut. 

# 2.
# Maintenant, on peut cree une variable de ton type! 
# Comme avant, tu creais une variable du type 'List':
l = [1,2,3]
# ou, rappele-toi:
l = List( [1,2,3] )
# Une variable du type 'Emotion':
e = Emotion(  )
# Essai d'imprimer cette emotion:
print 'Ma emotion: ', e  ### <-------- essai dans Python Console pour voir ce que ca donne
# Pas jolie? On vas ameliorer ca bientot

# 3.
# On commence a remplir ta classe...
# Qu'est ce que on peut rajouter?
# Qu'a-t-elle chaque emotion? Un nom!
# Quand tu cree une emotion tu veux dire laquelle...

class Emotion:
    def __init__(self, nom):
        self.name = nom

    def __str__(self):
        # Remplace la valeur que la fonction __str__ retourne
        # pour que ca soit plus jolie
        return  self.name+'qqqq'  ### <--- TON CODE ICI:

# Cree une variable de ton type 'Emotion' (de ta classe 'Emotion')
e2 = Emotion('happy')
# Essai d'imprimer cette emotion:
print 'Mon emotion: ', e2  ### <-------- essai dans Python Console pour voir ce que ca donne
print 'Le nom de mon emotion: ', e2.name  ### <-------- essai dans Python Console pour voir ce que ca donne

# 
