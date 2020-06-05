from Derivator import Derivator

def f(x):
    return x**3

derivator = Derivator(f)

fPrime = derivator.returnDerivate()

a = int(input("Borne de début >"))
b = int(input("Borne de fin >"))

derivator.findCommon(a, b)    