import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EstruturaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Manipulador de Estruturas de Dados")
        self.root.geometry("600x400")
        self.root.configure(bg="#F0F0F0")
        
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        
        # Abas
        self.lista_frame = tk.Frame(self.notebook, bg="#FFDDC1")
        self.fila_frame = tk.Frame(self.notebook, bg="#C1FFD7")
        self.pilha_frame = tk.Frame(self.notebook, bg="#C1D4FF")
        
        self.notebook.add(self.lista_frame, text="Lista")
        self.notebook.add(self.fila_frame, text="Fila")
        self.notebook.add(self.pilha_frame, text="Pilha")
        
        # Inicializar estruturas
        self.lista = []
        self.fila = []
        self.pilha = []
        
        # Montar interfaces
        self.build_lista()
        self.build_fila()
        self.build_pilha()

    def build_lista(self):
        tk.Label(self.lista_frame, text="Manipulação de Lista", bg="#FFDDC1", font=("Arial", 16)).pack(pady=10)
        self.lista_input = tk.Entry(self.lista_frame, font=("Arial", 12))
        self.lista_input.pack(pady=5)
        tk.Button(self.lista_frame, text="Adicionar", bg="#FFB085", command=self.add_lista).pack(pady=5)
        tk.Button(self.lista_frame, text="Remover", bg="#FFB085", command=self.remove_lista).pack(pady=5)
        self.lista_display = tk.Listbox(self.lista_frame, font=("Arial", 12), height=10)
        self.lista_display.pack(pady=10)
    
    def add_lista(self):
        item = self.lista_input.get()
        if item:
            self.lista.append(item)
            self.update_lista_display()
            self.lista_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite um valor para adicionar.")
    
    def remove_lista(self):
        selected = self.lista_display.curselection()
        if selected:
            self.lista.pop(selected[0])
            self.update_lista_display()
        else:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
    
    def update_lista_display(self):
        self.lista_display.delete(0, tk.END)
        for item in self.lista:
            self.lista_display.insert(tk.END, item)

    def build_fila(self):
        tk.Label(self.fila_frame, text="Manipulação de Fila", bg="#C1FFD7", font=("Arial", 16)).pack(pady=10)
        self.fila_input = tk.Entry(self.fila_frame, font=("Arial", 12))
        self.fila_input.pack(pady=5)
        tk.Button(self.fila_frame, text="Adicionar", bg="#A1FFC5", command=self.add_fila).pack(pady=5)
        tk.Button(self.fila_frame, text="Remover", bg="#A1FFC5", command=self.remove_fila).pack(pady=5)
        self.fila_display = tk.Listbox(self.fila_frame, font=("Arial", 12), height=10)
        self.fila_display.pack(pady=10)
    
    def add_fila(self):
        item = self.fila_input.get()
        if item:
            self.fila.append(item)
            self.update_fila_display()
            self.fila_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite um valor para adicionar.")
    
    def remove_fila(self):
        if self.fila:
            self.fila.pop(0)
            self.update_fila_display()
        else:
            messagebox.showwarning("Aviso", "A fila está vazia.")
    
    def update_fila_display(self):
        self.fila_display.delete(0, tk.END)
        for item in self.fila:
            self.fila_display.insert(tk.END, item)

    def build_pilha(self):
        tk.Label(self.pilha_frame, text="Manipulação de Pilha", bg="#C1D4FF", font=("Arial", 16)).pack(pady=10)
        self.pilha_input = tk.Entry(self.pilha_frame, font=("Arial", 12))
        self.pilha_input.pack(pady=5)
        tk.Button(self.pilha_frame, text="Adicionar", bg="#A1C7FF", command=self.add_pilha).pack(pady=5)
        tk.Button(self.pilha_frame, text="Remover", bg="#A1C7FF", command=self.remove_pilha).pack(pady=5)
        self.pilha_display = tk.Listbox(self.pilha_frame, font=("Arial", 12), height=10)
        self.pilha_display.pack(pady=10)
    
    def add_pilha(self):
        item = self.pilha_input.get()
        if item:
            self.pilha.append(item)
            self.update_pilha_display()
            self.pilha_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite um valor para adicionar.")
    
    def remove_pilha(self):
        if self.pilha:
            self.pilha.pop()
            self.update_pilha_display()
        else:
            messagebox.showwarning("Aviso", "A pilha está vazia.")
    
    def update_pilha_display(self):
        self.pilha_display.delete(0, tk.END)
        for item in reversed(self.pilha):
            self.pilha_display.insert(tk.END, item)

# Executar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = EstruturaGUI(root)
    root.mainloop()
