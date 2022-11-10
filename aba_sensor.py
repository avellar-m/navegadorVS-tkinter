# Aba do CLP

import tkinter.ttk as ttk
import random

class Aba(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.polinomio = [] # lista que contem os parametros do polinomio
        self.voltagem = 3.0
        self.temperatura = 100.0
        self.create_widgets() # chama a função que cria as widgets
    
    def create_widgets(self):
        self.tempLabel = ttk.Label(self, text = "Primeiro, defina as variáveis de interpolação")
        self.tick_variavel()
        self.atualizar_label()
        self.tempLabel.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    def atualizar_label(self):
        if len(self.polinomio) < 2:
            self.tempLabel.config(text = "Primeiro, defina as variáveis de interpolação")
        else:
            self.atualizar_temperatura()
            self.tempLabel.config(text = "Voltagem: {}, Temperatura: {}".format(self.voltagem, self.temperatura))
        self.after(2000, self.atualizar_label)
        print(self.polinomio)
    
    def tick_variavel(self):
        self.voltagem += random.uniform(-0.2, 0.2)
        if self.voltagem > 5:
            self.voltagem = 5
        elif self.voltagem < 0:
            self.voltagem = 0
        self.after(2000, self.tick_variavel)
    
    def atualizar_temperatura(self):
        self.atualizar_polinomio()
        self.temperatura = 0.0
        for i in range(len(self.polinomio)):
            self.temperatura += self.polinomio[i] * self.voltagem ** i
    
    def atualizar_polinomio(self):
        self.polinomio = self.master.master.polinomio
