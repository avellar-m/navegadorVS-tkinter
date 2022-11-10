import tkinter as tk
import tkinter.ttk as ttk

import styles
import aba_interpol, aba_sensor

class MainApplication(ttk.Frame):
    # Classe que define a interface principal do App

    def __init__(self, master):
        self.master = master
        ttk.Frame.__init__(self, self.master)
        self.style = ttk.Style(self)
        self.polinomio = []
        self.configure_style() # chama a função que configura a aparência da GUI
        self.configure_gui() # chama a função que define as propriedades da GUI
        self.create_widgets() # chama a função que cria as widgets
        self.pack()
   
    def configure_gui(self):
        # Customiza a janela:
        #self.master.geometry("246x465")
        self.master.title("Navegador VS")
        self.master.resizable(width = False, height = False)
    
    def configure_style(self):
        # Customiza o tema da interface
        styles.configurar_estilo(self.style)

    def create_widgets(self):
        # Cria um controlador5 de abas (widget Notebook):
        self.tabControl = ttk.Notebook(self)
        self.aba1 = aba_sensor.Aba(self.tabControl)
        self.aba2 = aba_interpol.Aba(self.tabControl)
        self.tabControl.add(self.aba1, text = "Sensor")
        self.tabControl.add(self.aba2, text = "Interpolação")
        self.tabControl.pack(expand = 1, fill = "both")
    
    def atualizar_polinomio(self):
        self.aba1.polinomio = self.aba2.polinomio
        self.after(200, self.atualizar_polinomio)

if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call("lappend", "auto_path", "./awthemes-10.4.0")
    root.tk.call("package", "require", "awlight")
    main_app =  MainApplication(root)
    root.mainloop()
