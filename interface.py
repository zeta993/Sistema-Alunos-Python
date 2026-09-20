import customtkinter as ctk
import main
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.conn,self.cursor=main.Banco_de_dados()
        self.title('Cadastro de alunos')
        self.geometry('1050x750')
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.barra_lateral = ctk.CTkFrame(self,width = 250)
        self.barra_lateral.grid(row=0, column=0,sticky="nsew",padx=(0,15))
        self.principal=ctk.CTkFrame(self,width=500)
        self.principal.grid(row=0, column=1,sticky="nsew")
        self.cria_Dash()

    def limpar_principal(self):
     for elemento in self.principal.winfo_children():
        elemento.destroy()

    def cria_Dash(self):
        self.titulo=ctk.CTkLabel(self.barra_lateral,text='Dashboard',font=ctk.CTkFont(size=24,weight=("bold")))
        self.titulo.pack(pady=(10,10), padx=(40,40))

        self.botao=ctk.CTkButton(self.barra_lateral, text ='Painel de controle', command=self.cria_Sele)
        self.botao.pack(pady=(80,10), padx=(50,50))

        self.botao2=ctk.CTkButton(self.barra_lateral, text ='Graficos',command=self.cria_graf)
        self.botao2.pack(pady=(30,10), padx=(50,50))

        self.botao3=ctk.CTkButton(self.barra_lateral, text ='Alterar dados',command=self.cria_opc)
        self.botao3.pack(pady=(30,10), padx=(50,50))

        self.botao4=ctk.CTkButton(self.barra_lateral, text ='Encerrar sistema',command=self.fechar)
        self.botao4.pack(pady=(30,10), padx=(50,50))

        self.assinatura=ctk.CTkLabel(self.barra_lateral, text='vinicius dias')
        self.assinatura.pack(pady=(300,0))
    def fechar(self):
       main.Fechar_banco(self.conn)
       self.destroy()
    def cria_Sele(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text="Painel de Controle", font=ctk.CTkFont(size=24,weight=('bold')))
        self.titulo.pack(pady=(30,0))
        self.botao1=ctk.CTkButton(self.principal,text="Cadastrar Aluno",command=self.cadastrar)
        self.botao1.pack(pady=(200,60))
        self.botao2=ctk.CTkButton(self.principal,text="Consultar ficha",command=self.fichas)
        self.botao2.pack(pady=(0,60))
        self.botao3=ctk.CTkButton(self.principal,text="Registrar Pagamento",command=self.pagamento)
        self.botao3.pack(pady=(0,60))
        self.botao4=ctk.CTkButton(self.principal,text="Cadastrar Aluno Premium",command=self.premium)
        self.botao4.pack(pady=(0,60))

    def cria_opc(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text='Alteração de dados',font=ctk.CTkFont(size=25,weight=('bold')))
        self.titulo.pack(pady=30)
        self.camporg=ctk.CTkEntry(self.principal,placeholder_text='Insira o RG')
        self.camporg.pack(pady=200)
        self.botao1=ctk.CTkButton(self.principal,text="Entrar",command=self.validar)
        self.botao1.pack(pady=10)

    def cria_term(self):
        pass

    def cria_graf(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text="Ainda em construçao", font=ctk.CTkFont(size=40,weight=("bold")))
        self.titulo.pack(pady=300)

    def validar(self):
      try :
        rg = int(self.camporg.get())
        val,d1,d2,d3,d4,d5,d6=main.consultar_ficha(self.cursor,rg)
        if val:
         self.Mostrar_dados(d1,d2,d3,d4,d5,d6)
        else:
         print("rg nao cadastrado na base de dados")
         return
      except ValueError:
               print('rg invalido')
               return
    def Mostrar_dados(self,d1,d2,d3,d4,d5,d6):
       self.limpar_principal()
       self.RG=ctk.CTkLabel(self.principal,text=f'RG: {d1}',font=ctk.CTkFont(size=20))
       self.RG.pack(pady=(100,10))
       self.Nome=ctk.CTkLabel(self.principal,text=f'Nome: {d2}',font=ctk.CTkFont(size=20))
       self.Nome.pack(pady=10)
       self.Idade=ctk.CTkLabel(self.principal,text=f'Idade: {d3}',font=ctk.CTkFont(size=20))
       self.Idade.pack(pady=10)
       self.genero=ctk.CTkLabel(self.principal,text=f'Genero: {d4}',font=ctk.CTkFont(size=20))
       self.genero.pack(pady=10)
       if d5:
        self.premium=ctk.CTkLabel(self.principal,text=f'--------Aluno premium:-------',font=ctk.CTkFont(size=40))
        self.premium.pack(pady=20)
       else:
          if d6:
           self.adimplent=ctk.CTkLabel(self.principal,text="O aluno esta adimplente")
           self.adimplent.pack(pady=20)
          else:
             self.adimplent=ctk.CTkLabel(self.principal,text="O aluno esta inadimplente")
             self.adimplent.pack(pady=20)

    def cadastrar(self):
       self.limpar_principal()
       self.titulo=ctk.CTkLabel(self.principal,text='Cadastro de novo aluno')
       self.titulo.pack(pady=50)
       self.campo1=ctk.CTkEntry(self.principal,placeholder_text='RG')
       self.campo1.pack(pady=15)
       self.campo2=ctk.CTkEntry(self.principal,placeholder_text='Nome')
       self.campo2.pack(pady=15)
       self.campo3=ctk.CTkEntry(self.principal,placeholder_text='Idade')
       self.campo3.pack(pady=15)
       self.campo4=ctk.CTkEntry(self.principal,placeholder_text='Genero')
       self.campo4.pack(pady=15)
       self.botao1=ctk.CTkButton(self.principal,text="Salvar",command=lambda:self.confirmaçao(False))
       self.botao1.pack(pady=25)

    def premium(self):
       self.limpar_principal()
       self.titulo=ctk.CTkLabel(self.principal,text='Cadastro de novo aluno')
       self.titulo.pack(pady=50)
       self.campo1=ctk.CTkEntry(self.principal,placeholder_text='RG')
       self.campo1.pack(pady=15)
       self.campo2=ctk.CTkEntry(self.principal,placeholder_text='Nome')
       self.campo2.pack(pady=15)
       self.campo3=ctk.CTkEntry(self.principal,placeholder_text='Idade')
       self.campo3.pack(pady=15)
       self.campo4=ctk.CTkEntry(self.principal,placeholder_text='Genero')
       self.campo4.pack(pady=15)
       self.botao1=ctk.CTkButton(self.principal,text="Salvar",command=lambda:self.confirmaçao(True))
       self.botao1.pack(pady=25)

    def confirmaçao(self,premium):
      try :
       rg = int(self.campo1.get())
      except ValueError:
        print('rg invalido')
        return
      nome = self.campo2.get()
      try:
        idade = int(self.campo3.get())
      except ValueError:
        print('idade invalida')
        return
      genero = self.campo4.get()
      if premium:
         valida=main.cadastrar_premium(self.conn,self.cursor,rg,nome,idade,genero)
      else:
         valida=main.cadastrar_pessoa(self.conn,self.cursor,rg,nome,idade,genero)   
      if valida:
         self.titulo=ctk.CTkLabel(self.principal,text='Cadastrado com sucesso')
         self.titulo.pack(pady=150)
      else:
         self.titulo=ctk.CTkLabel(self.principal,text='RG Ja Cadastrado')
         self.titulo.pack(pady=150)
     
     

    def fichas(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text='Consultar ficha')
        self.titulo.pack(pady=50) 
        self.camporg=ctk.CTkEntry(self.principal,placeholder_text='Insira o RG')
        self.camporg.pack(pady=200)
        self.botao1=ctk.CTkButton(self.principal,text="Entrar",command=self.validar)
        self.botao1.pack(pady=10)
       
    def pagamento(self):
     self.limpar_principal()
     self.titulo = ctk.CTkLabel(self.principal,text='Registrar pagamento')
     self.titulo.pack(pady=50)
     self.camporg = ctk.CTkEntry(self.principal,placeholder_text='Insira o RG')
     self.camporg.pack(pady=200)
     self.botao1 = ctk.CTkButton(self.principal,text="Entrar",command=self.confirmar_pagamento)
     self.botao1.pack(pady=10)

    def confirmar_pagamento(self):
     try:
      rg = int(self.camporg.get())
     except ValueError:
      print("RG inválido")
      return
     val,rg,nome,existe=main.registrar_pagamento(self.conn,self.cursor,rg)
     self.limpar_principal()
     if existe:
        if val:
         self.titulo = ctk.CTkLabel(self.principal,text=f'O pagamento de {nome}, RG: {rg}, foi registrado com sucesso')
         self.titulo.pack(pady=150)
        else:
         self.titulo = ctk.CTkLabel(self.principal,text=f'{nome}, RG: {rg}, é aluno PREMIUM e não paga mensalidade')
         self.titulo.pack(pady=150)
     else:
        self.titulo = ctk.CTkLabel(self.principal,text='Aluno não cadastrado em nossa base de dados')
        self.titulo.pack(pady=150)
janela=app()

janela.mainloop()