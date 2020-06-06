from tkinter import *
from Derivator import Derivator

#La classe qui gère l'interface utilisateur
class Interface():
    def __init__(self):

        #Initialisation de la fenêtre
        self.window = Tk()
        self.window.title("DerivateTools")
        self.window.geometry("1080x720")

        #Ajout des composants
        self.Frame1 = LabelFrame(self.window, text="Fonction")
        self.Frame2 = Frame(self.window)
        
        self.AValue = StringVar()
        self.InputA = Entry(self.Frame1, textvariable=self.AValue, width=5)
        self.x3 = Label(self.Frame1, text="x^3 + ")

        self.BValue = StringVar()
        self.InputB = Entry(self.Frame1, textvariable=self.BValue, width=5)
        self.x2 = Label(self.Frame1, text="x^2 + ")

        self.CValue = StringVar()
        self.InputC = Entry(self.Frame1, textvariable=self.CValue, width=5)
        self.x = Label(self.Frame1, text="x + ")

        self.DValue = StringVar()
        self.InputD = Entry(self.Frame1, textvariable=self.DValue, width=5)
        
        self.FunButton = Button(self.Frame1, text="Dériver", command=self.funDerive)

        self.Frame3 = LabelFrame(self.window, text="Quand est-ce que la fonction est égale à sa dérivée ?")
        self.a = StringVar()
        self.BorneA = Entry(self.Frame3, textvariable=a).grid
        self.b = StringVar()
        self.BorneB = Entry(self.Frame3, textvariable=self.b)
        self.CalcuButton = Button(self.Frame3, text="Calculer", command=self.find)

        self.start()    

    def funDerive(self):
        valueA = float(self.AValue.get())
        valueB = float(self.BValue.get())
        valueC = float(self.CValue.get())
        valueD = float(self.DValue.get())
        
        self.fun = lambda x: valueA*x**3 + valueB*x**2 + valueC*x + valueD

        #Initialisation du composant de dérivation
        self.derivator = Derivator(self.fun)
        
        #Dérivation de la fonction et enregistrement sous deux formes : textuelle et lambda
        self.derivate = self.derivator.returnDerivate()
        self.txtDerivate = self.derivator.derivate()

        #Affichage du résultat à l'utilisateur
        string = "Dérivée : " + str(self.txtDerivate)
        self.Result = Label(self.Frame2, text=string) 
        self.Result.pack()
    
    def find(self):
        a = 
        points = self.derivator.findCommon()

    def start(self):
        self.Frame1.pack(fill=X, side=TOP, padx=10)
        self.InputA.pack(side=LEFT, padx=2)
        self.x3.pack(side=LEFT)
        self.InputB.pack(side=LEFT)
        self.x2.pack(side=LEFT)
        self.InputC.pack(side=LEFT)
        self.x.pack(side=LEFT)
        self.InputD.pack(side=LEFT)
        self.FunButton.pack(side=RIGHT, padx=2, fill=Y)
        self.Frame2.pack()
        self.window.mainloop()

#Debug Part

inter = Interface()