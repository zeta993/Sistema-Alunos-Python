import customtkinter as ctk
import main
import graficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

        self.botao5=ctk.CTkButton(self.barra_lateral, text ='Apagar cadastro',command=self.preview)
        self.botao5.pack(pady=(30,10), padx=(50,50))

        self.botao4=ctk.CTkButton(self.barra_lateral, text ='Encerrar sistema',command=self.fechar)
        self.botao4.pack(pady=(30,10), padx=(50,50))

        self.assinatura=ctk.CTkLabel(self.barra_lateral, text='vinicius dias')
        self.assinatura.pack(pady=(300,0))
    def preview(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text='DELETAR CADASTRO')
        self.titulo.pack(pady=50) 
        self.camporg=ctk.CTkEntry(self.principal,placeholder_text='Insira o RG')
        self.camporg.pack(pady=200)
        self.botao1=ctk.CTkButton(self.principal,text="Entrar",command=lambda:self.validar('deletar'))
        self.botao1.pack(pady=10)




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

    def cria_opc(self):
        self.limpar_principal()
        self.titulo=ctk.CTkLabel(self.principal,text='Alteração de dados',font=ctk.CTkFont(size=25,weight=('bold')))
        self.titulo.pack(pady=30)
        self.camporg=ctk.CTkEntry(self.principal,placeholder_text='Insira o RG')
        self.camporg.pack(pady=200)
        self.botao1=ctk.CTkButton(self.principal,text="Entrar",command=lambda:self.validar('editar'))
        self.botao1.pack(pady=10)

    def cria_term(self, rg, nome, idade, genero, premium, adimp):
     self.limpar_principal()
     self.titulo = ctk.CTkLabel(self.principal,text="Alterar dados",font=ctk.CTkFont(size=25, weight="bold"))
     self.titulo.pack(pady=30)
     self.rg = ctk.CTkLabel(self.principal,text=f"RG: {rg}")
     self.rg.pack(pady=10)
     self.linha_nome=ctk.CTkFrame(self.principal)
     self.linha_nome.pack(pady=30)
     self.campo_nome = ctk.CTkEntry(self.linha_nome,width=250)
     self.campo_nome.insert(0, nome)
     self.campo_nome.configure(state="disabled")
     self.campo_nome.pack(side="left", padx=5)
     self.botao_editar_nome = ctk.CTkButton(self.linha_nome,text="✎",width=40,command=lambda: self.desbloquear(self.campo_nome))
     self.botao_editar_nome.pack(side="left", padx=5)

     self.linha_idade=ctk.CTkFrame(self.principal)
     self.linha_idade.pack(pady=30)
     self.campo_idade = ctk.CTkEntry(self.linha_idade,width=250)
     self.campo_idade.insert(0, idade)
     self.campo_idade.configure(state="disabled")
     self.campo_idade.pack(side="left", padx=5)
     self.botao_editar_idade = ctk.CTkButton(self.linha_idade,text="✎",width=40,command=lambda: self.desbloquear(self.campo_idade))
     self.botao_editar_idade.pack(side="left", padx=5)

     self.linha_genero=ctk.CTkFrame(self.principal)
     self.linha_genero.pack(pady=30)
     self.campo_genero = ctk.CTkOptionMenu(self.linha_genero,values=["Masculino","Feminino","Prefiro não informar"],width=250)
     self.campo_genero.set(genero)
     self.campo_genero.configure(state="disabled")
     self.campo_genero.pack(side="left", padx=5)
     self.botao_editar_genero = ctk.CTkButton(self.linha_genero,text="✎",width=40,command=lambda: self.desbloquear(self.campo_genero))
     self.botao_editar_genero.pack(side="left", padx=5)
     
     self.linha_premium=ctk.CTkFrame(self.principal)
     self.linha_premium.pack(pady=30)
     self.campo_premium = ctk.CTkSwitch(self.linha_premium,text="premium",width=250)
     if premium:
      self.campo_premium.select()
     self.campo_premium.configure(state="disabled")
     self.campo_premium.pack(side="left", padx=5)
     self.botao_editar_premium = ctk.CTkButton(self.linha_premium,text="✎",width=40,command=lambda: self.desbloquear(self.campo_premium))
     self.botao_editar_premium.pack(side="left", padx=5)
     self.botao_salvar = ctk.CTkButton(self.principal,text="Salvar alterações",command=lambda:self.alterar_dados(rg,adimp))
     self.botao_salvar.pack(pady=30)

    def desbloquear(self,campo):
      campo.configure(state="normal")
      campo.focus()

    def cria_graf(self):
        self.limpar_principal()
        self.grafico_opçao = ctk.CTkOptionMenu(self.principal,values=["Todos os alunos","Numero de alunos por idade","Alunos por genero","Percentual de adimplencia"])
        self.grafico_opçao.pack(pady=100)
        self.botao1=ctk.CTkButton(self.principal,text="Salvar",command=self.gerar_graficos)
        self.botao1.pack(pady=25)
      

    def validar(self,açao):
      try :
        rg = int(self.camporg.get())
        val,d1,d2,d3,d4,d5,d6=main.consultar_ficha(self.cursor,rg)
        if val:
         if açao=='consultar':
          self.Mostrar_dados(d1,d2,d3,d4,d5,d6,açao)
         elif açao=='deletar':
           self.Mostrar_dados(d1,d2,d3,d4,d5,d6,açao)
         else:
           self.cria_term(d1,d2,d3,d4,d5,d6)
        else:
         erro = ctk.CTkLabel(self.principal,text="RG não cadastrado na base de dados")
         erro.pack(pady=10)
        return
      except ValueError:erro = ctk.CTkLabel(self.principal,text="RG inválido")
      erro.pack(pady=10)
      return

    def alterar_dados(self,rg,adimp):
      d2=self.campo_nome.get()
      try:
        d3 = int(self.campo_idade.get())
      except ValueError:
        erro = ctk.CTkLabel(self.principal,text="Idade inválida")
        erro.pack(pady=10)
        return
      d4=self.campo_genero.get()
      d5=self.campo_premium.get()

      confirm=main.alterar_dados(self.cursor,self.conn,d2,d3,d4,d5,adimp,rg)
      if confirm:
        confirmado=ctk.CTkLabel(self.principal,text='alterado com sucesso')
        confirmado.pack(pady=15)


    def Mostrar_dados(self,d1,d2,d3,d4,d5,d6,açao):
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
       if açao == 'deletar':
        self.botao_deletar=ctk.CTkButton(self.principal,text="Deletar cadastro", command=lambda:self.deletar(d1))
        self.botao_deletar.pack(pady=30)

    def deletar(self,rg):
     pas = main.deletar(self.conn, self.cursor, rg)
     if pas:
        self.limpar_principal()
        confirmado = ctk.CTkLabel(self.principal,text="Usuário deletado com sucesso")
        confirmado.pack(pady=150)

    def gerar_graficos(self):
     d = self.grafico_opçao.get()
     if d == "Todos os alunos":
       df = graficos.Grafico_geral(self.cursor)
       tabela = ctk.CTkFrame(self.principal)
       tabela.pack(padx=20, pady=20)
       for posicao, coluna in enumerate(df.columns):
         titulo = ctk.CTkLabel(tabela, text=coluna)
         titulo.grid(row=0, column=posicao, padx=10, pady=10)
       for indice, aluno in df.iterrows():
        for posicao, valor in enumerate(aluno):
         coluna = df.columns[posicao]
         if coluna == "Premium" or coluna == "Adimplente":
          if valor == 1:
           valor = "Sim"
          else:
           valor = "Não"
         dado = ctk.CTkLabel(tabela, text=valor)
         dado.grid(row=indice + 1,column=posicao,padx=10,pady=5)
     elif d=="Numero de alunos por idade":
      fig=graficos.Grafico_de_idades(self.cursor)
      canvas=FigureCanvasTkAgg(fig, master=self.principal)
      canvas.get_tk_widget().pack(fill='both',pady=30,padx=30,expand=True)
     elif d =="Alunos por genero":
          fig=graficos.Grafico_de_generos(self.cursor)
          canvas = FigureCanvasTkAgg(fig, master=self.principal)
          canvas.get_tk_widget().pack(fill='both',pady=30,padx=30,expand=True)

     elif d =="Percentual de adimplencia":
          fig=graficos.Grafico_de_adimplencia(self.cursor)
          canvas = FigureCanvasTkAgg(fig, master=self.principal)
          canvas.get_tk_widget().pack(fill='both',pady=30,padx=30,expand=True)
       
    
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
       self.genero_opçao = ctk.CTkOptionMenu(self.principal,values=["Masculino", "Feminino", "Prefiro não informar"])
       self.genero_opçao.pack(pady=15)
       self.switc=ctk.CTkSwitch(self.principal,text="Aluno premium")
       self.switc.pack(pady=(0,10))
       self.botao1=ctk.CTkButton(self.principal,text="Salvar",command=self.confirmaçao)
       self.botao1.pack(pady=25)

    def confirmaçao(self):
      try :
       rg = int(self.campo1.get())
      except ValueError:
       erro = ctk.CTkLabel(self.principal, text="RG inválido")
       erro.pack(pady=10)
       return
      nome = self.campo2.get()
      try:
        idade = int(self.campo3.get())
      except ValueError:
       erro = ctk.CTkLabel(self.principal, text="Idade inválida")
       erro.pack(pady=10)
       return
      genero = self.genero_opçao.get()
      if self.switc.get():
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
        self.botao1=ctk.CTkButton(self.principal,text="Entrar",command=lambda:self.validar('consultar'))
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
      erro = ctk.CTkLabel(self.principal, text="RG inválido")
      erro.pack(pady=10)
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