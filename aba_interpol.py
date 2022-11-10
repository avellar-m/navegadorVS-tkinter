# Aba de interpolação

import tkinter as tk
import tkinter.ttk as ttk

import interpol

class Aba(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.polinomio = [] # lista que contem os parametros do polinomio
        self.create_widgets() # chama a função que cria as widgets
    
    def create_widgets(self):
        self.grauBox = ttk.Spinbox(self, from_=1, to=5, width=1, command=self.atualizar_entries)
        self.grauBox.set(1)
        self.grauBox.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.grauLabel = ttk.Label(self, text = "Grau do polinômio:")
        self.grauLabel.grid(row = 0, column = 0)
        
        self.voltLabel = ttk.Label(self, text = "V")
        self.voltLabel.grid(row = 1, column = 0)
        self.resultadoLabel = ttk.Label(self, text = "Resultado")
        self.resultadoLabel.grid(row = 1, column = 1)
        
        self.voltEntry, self.resultadoEntry = [], []
        for i in range(6):
            self.voltEntry.append(ttk.Entry(self))
            self.resultadoEntry.append(ttk.Entry(self))
            self.voltEntry[-1].grid(row = i+2, column = 0)
            self.resultadoEntry[-1].grid(row = i+2, column = 1)
        
        self.atualizar_entries()
        
        self.interpolButton = ttk.Button(self, text = "atualizar polinômio", command = self.atualizar_polinomio)
        self.interpolButton.grid(row = 8, column = 0, padx = 10, pady = 10)
    
    def atualizar_polinomio(self):
        x, y = [], []
        grau = int(self.grauBox.get())
        for i in range(grau + 1):
            try:
                x.append(float(self.voltEntry[i].get()))
                y.append(float(self.resultadoEntry[i].get()))
            except:
                print("valor da coluna {} está errado. tente novamente".format(i))
        self.polinomio = interpol.interpol(x, y)
        self.master.master.polinomio = self.polinomio
        self.master.master.aba1.atualizar_polinomio()
        self.master.master.aba1.atualizar_label()
        
    def atualizar_entries(self):
        # deixa algumas caixas cinza de acordo com o grau do polinômio
        grau = int(self.grauBox.get())
        for i in range(grau + 1):
            self.voltEntry[i].config(state = "normal")
            self.resultadoEntry[i].config(state = "normal")
        for i in range(grau + 1, 6):
            self.voltEntry[i].config(state = "disabled")
            self.resultadoEntry[i].config(state = "disabled")
        
        
