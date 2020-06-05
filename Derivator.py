from sympy import Symbol, diff, lambdify
import numpy

class Derivator():
    def __init__(self, fun, degr = 1):
        self.fun = fun
        self.var = Symbol('x')
        self.degr = degr
    
    def derivate(self):
        return diff(self.fun(self.var), self.var, self.degr)
    
    def returnDerivate(self):
        self.prime = lambdify(self.var, self.derivate(), "numpy")
        return self.prime
    
    def findCommon(self, a, b):
        for i in range(a, b):
            if self.fun(i) == self.prime(i):
                print("Pour " + str(i) + ", la fonction et sa dérivée ont la même valeur.")

