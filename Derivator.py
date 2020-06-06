from sympy import Symbol, diff, lambdify
import numpy

#La classe qui fera tout le travail
class Derivator():
    def __init__(self, fun, degr = 1):
        self.fun = fun
        self.var = Symbol('x')
        self.degr = degr
    
    #Méthode de base qui dérive un fonction donnée dans le constructeur
    def derivate(self):
        return diff(self.fun(self.var), self.var, self.degr)
    
    #Méthode qui convertit la dérivée obtenue au format sympy en une fonction utilisable
    def returnDerivate(self):
        self.prime = lambdify(self.var, self.derivate(), "numpy")
        return self.prime
    
    #Méthode qui permet de savoir si, dans un intervalle donné, il existe un entier pour lequel la fonction et sa dérivée ont la même valeur
    def findCommon(self, a, b):
        commons = []
        for i in range(a, b):
            if self.fun(i) == self.prime(i):
                commons.append(i)
        return commons
