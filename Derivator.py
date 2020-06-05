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
        return lambdify(self.var, self.derivate(), "numpy")
    
    def findCommon(self):
        return
