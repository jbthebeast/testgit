#coding:utf-8

""" 
nommer une variable : doit commcer par une lettre
						ne dois pas contenir de caractère 
						ne pas contenir d'espace
						utiliser le tiret du bas (_)
Types standars		:	entier num (int)
						nombre flotant, a virgule (float)
						chaine de caractaire (str)
						booléen 0 ou 1 (bool)
						autre ( liste, dico,tuples)
fonctions vues : print
				input
				type
				int( ex : 2), float (ex : 2.5), str, bool,
				str.format
opération en python : +
						-
						*
						/
						% (modulo) reste d'une division euclidienne

variable = variable + X
variable + = X

Varaible = Variable - X
Variable = variable * X
Variable*= X
opérateur comparaison : == (égal à), != ( différent de), <(plus petit que), >(plus grand que), >=, <=
Condition multiple : and(et), or(ou), in / not in (dans / pas dans)
Mots clef condition : if / elif / else
Boucle : while/ for
Mots clés : break (casse la boucle) / continue (reveient au début de la boucle)
"""
#création d'un petit combats entre deux personnes

player1 = input("Choisissez un nom de joueur : ")

player2 = input("Choisissez un nom de joueur : ")

print("Bon combat {} et {}, vous avez 100 points de vie".format(player1, player2))

viePlayer1 = 100
viePlayer2 = 100

listeDesAttaques = "feu, eau, volt, pierre"

print("Voici les attaques disponibles : {}".format(listeDesAttaques))

#dommage des attaques
feu = 25
eau = 05
volt = 19
pierre = 6

#debut du combat

JeuLance = True

while JeuLance :
	votreAttaque = input("Choisissez votre attaques : ")

	if votreAttaque == "feu":
		print("-15 pour le player2")

	if votreAttaque == "eau":
		print("-16 pour le player2")
		
	if votreAttaque == "volt":
		print("-19 pour le player2")
		
	if votreAttaque == "pierre":
		print("-6 point pour le player2")

	if votreAttaque =="quit":
		break	

print("a plus")
