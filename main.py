from Derivator import Derivator

def f(x):
    return x**10

derivator = Derivator(f)

fPrime = derivator.returnDerivate()

a = int(input("Borne de début >"))
b = int(input("Borne de fin >"))

derivator.findCommon(a, b)

#On peut dégager de ce programme que pour une fonction mononome de degré n, la fonction et sa dérivée ont la même valeur en deux points : 0 et n