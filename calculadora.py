import tkinter as tk

class CalculadoraApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora")

        self.entrada = tk.Entry(janela, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        linha, coluna = 1, 0
        for btn in botoes:
            comando = lambda x=btn: self.clique(x)
            tk.Button(janela, text=btn, width=5, height=2, font=("Arial", 18),
                      command=comando).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        tk.Button(janela, text='=', width=20, height=2, font=("Arial", 18),
                  command=self.calcular).grid(row=5, column=0, columnspan=4)

    def clique(self, valor):
        if valor == 'C':
            self.entrada.delete(0, tk.END)
        else:
            self.entrada.insert(tk.END, valor)

    def calcular(self):
        try:
            expressao = self.entrada.get()
            resultado = eval(expressao)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

class TesteCalculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            return "Erro"
        return a / b

if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraApp(janela)
    janela.mainloop()