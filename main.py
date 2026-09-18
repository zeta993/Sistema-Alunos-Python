Registros = {}

class Dados:
 def __init__ (self,name,age,gener,document,premium,adimp):
    self.name=name
    self.age=age
    self.gener=gener
    self.document=document
    self.premium=premium
    self.adimp=adimp

 def Buscar_Dados(self):
  print(f'Nome : {self.name}\nIdade : {self.age}\nGenero : {self.gener}\nRG : {self.document}')
  if self.adimp:
    print ('adimplente')
  else:
    print('inadimplente')

 def Pagamento(self):
  if self.premium:
   print('alunos premium nao pagam mensalidade')
  else:
   print(f'pagamento computado')
   self.adimp=True

 def salvar_dados(self):
  Registros[self.document]=self
  print('dados resgistrados com sucesso')

class AlunoPremium(Dados):

    def Buscar_Dados(self):
        print(f'Nome: {self.name}')
        print(f'Idade: {self.age}')
        print(f'Gênero: {self.gener}')
        print(f'Documento: {self.document}')
        print('----- ALUNO PREMIUM -----')

def solicitar_idade():
 testando=True
 while(testando):
  try:
    idade = int(input('Digita a sua idade'))
    return idade
  except ValueError:
    print('insira um numero valido')

def solicitar_rg():
 testando=True
 while(testando):
  try:
    rg = int(input('digite o seu rg'))
    return rg
  except ValueError:
    print('insira um numero valido')

def cadastrar_pessoa():
  Dado_1=solicitar_rg()
  if Dado_1 in Registros:
    print('esse rg ja esta cadastrado')
    return
  Dado_2=input('Qual seu nome? ')
  Dado_3=solicitar_idade()
  Dado_4=input('Qual seu genero ')
  nova_pessoa=Dados(Dado_2,Dado_3,Dado_4,Dado_1,False,True)
  nova_pessoa.salvar_dados()

def cadastrar_premium():
 Dado_1=solicitar_rg()
 if Dado_1 in Registros:
    print('esse rg ja esta cadastrado')
    return
 Dado_2=input('Qual seu nome? ')
 Dado_3=solicitar_idade()
 Dado_4=input('Qual seu genero ')
 nova_pessoa=AlunoPremium(Dado_2,Dado_3,Dado_4,Dado_1,True,True)
 nova_pessoa.salvar_dados()

def consultar_ficha():
   var=validar_rg()
   Registros[var].Buscar_Dados()

def registrar_pagamento():
   var=validar_rg()
   Registros[var].Pagamento()

def listar_alunos():
    print(f'Atualmente possuímos {len(Registros)} alunos cadastrados.')
    for document, aluno in Registros.items():
      if aluno.premium:
            premium = 'Sim'
      else:
            premium = 'Não'

      print(f'RG : {document}\nNome : {aluno.name}\npremium : {premium}')

def validar_rg():
 verificando_rg=True
 while(verificando_rg):
  try:
   rg = int(input('digite o rg...'))
   if rg in Registros:
     return rg
   else:
     print('Rg nao cadastrado na base de dados, tente novamente')
     continue
  except ValueError:
   print('digite apenas numeros')
   continue

def mostrar_menu():
    print('''
------ SISTEMA ------
[1] Cadastrar aluno
[2] Consultar ficha
[3] Registrar pagamento
[4] Lista de alunos
[5] Cadastro no premium
[6] Sair
---------------------
''')

def Solicitar_opcao():
  try:
   return int(input('Escolha uma opção: '))
  except ValueError:
   return 0

def Main():
 aberto=True
 while(aberto):
  mostrar_menu()
  opcao=Solicitar_opcao()
  if opcao == 1:
   cadastrar_pessoa()
  elif opcao == 2:
    consultar_ficha()
  elif opcao == 3:
    registrar_pagamento()
  elif opcao == 4:
    listar_alunos()
  elif opcao == 5:
    cadastrar_premium()
  elif opcao == 6:
    aberto = False
  else:
    print('por favor, tente uma opção valida')

Main()