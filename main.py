from Derivator import Derivator

def f(x):
    return x**2

derivator = Derivator(f)

fPrime = derivator.returnDerivate()

a = int(input("Borne de début >"))
b = int(input("Borne de fin >"))

for i in range(a, b):
    if f(i) == fPrime(i):
        print("True" + " pour x = " +  str(i))

    