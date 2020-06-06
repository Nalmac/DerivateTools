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
        self.Frame1 = LabelFrame(self.window, text="Bornes de calcul")
        self.Frame1.pack(fill=X, expand=YES)

    
    def start(self):
        self.window.mainloop()

#Debug Part

inter = Interface()
inter.start()