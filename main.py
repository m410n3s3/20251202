import tkinter as tk
import _sqlite3 as sq

class Controlador(tk.Frame):
    def __init__(self,JanPr):
        tk.Frame.__init__(self,JanPr)
        #chama um classe para construir uma página sobre a principal
        self.PagLogin = PaginaLogin(self)
        self.PagLogin.grid(row=0,column=0)

        #criaçao menu tela
        self.menu = TrocadorTela(self)
        self.menu.grid(row=1,column=0)

class TrocadorTela(tk.Frame):
    def __init__(self,JanPr):
        tk.Frame.__init__(self,JanPr)
        self.PagLogin = tk.Button(self,text="Login",height=2,width=16,command= self.master.PagLogin.tkraise)
        self.PagLogin.grid(row=0,column=0)



class PaginaLogin(tk.Frame):
    def __init__(self,JanPr):
        tk.Frame.__init__(self,JanPr)
        #Coloca um label para iniciar a pagina de login
        self.Label1=tk.Label(self, text = "Tela de Login", height= 5, width= 40, background= "Green")
        self.Label1.grid(row=0,column=0)
        #Nome de usuario e senha
        self.Label_Nome_Usuario = tk.Label(self,text="Nome de Usuário: ", height= 3, width= 15)
        self.Label_Nome_Usuario.grid(row=1,column=0)
        self.Entry_Nome_Usuario = tk.Entry(self)
        self.Entry_Nome_Usuario.grid(row=1,column=1)
        print(self.Entry_Nome_Usuario.get())

        self.Label_Senha_Usuario = tk.Label(self,text="Senha de Usuário: ", height= 3, width= 15)
        self.Label_Senha_Usuario.grid(row=2,column=0)
        self.Entry_Senha_Usuario = tk.Entry(self, show = "*")
        self.Entry_Senha_Usuario.grid(row=2,column=1)
        print(self.Entry_Senha_Usuario.get())




def main():
    JanelaPrincipal = tk.Tk()
    JanelaPrincipal.title("Banco Python")
    #criação de janela com 70% do tamanho da tela
    TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.7)
    TamVertJanela = int(JanelaPrincipal.winfo_screenheight()*0.7)
    print(TamHorJanela,TamVertJanela)
    TamTela = str(TamHorJanela)+"x"+str(TamVertJanela)
    JanelaPrincipal.geometry(TamTela)

    Pagina0 = Controlador(JanelaPrincipal)
    Pagina0.pack(expand=True, fill=tk.BOTH)
    JanelaPrincipal.mainloop()


if __name__ == "__main__":
    main()