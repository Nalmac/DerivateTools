from Derivator import Derivator

#Fonction de test
def f(x):
    return x**10

#Construction de la classe Derivator, avec la fonction f comme fonction de travail
derivator = Derivator(f)

#On récupère la dérivée sous forme de lambda (fonction stockée dans une variable)
fPrime = derivator.returnDerivate()

#On demande les bornes de début et de fin à l'utilisateur
a = int(input("Borne de début >"))
b = int(input("Borne de fin >"))

#On cherche s'il y a dans cet intervalle des nombres entiers tels que f(x) = f'(x)
derivator.findCommon(a, b)

#On peut dégager de ce programme que pour une fonction mononome de degré n, la fonction et sa dérivée ont la même valeur en deux points : 0 et n