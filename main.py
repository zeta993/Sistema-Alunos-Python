
def solicitar_idade():
 while True:
  try:
    idade = int(input('Digita a sua idade'))
    return idade
  except ValueError:
    print('insira um numero valido')

def solicitar_rg():
 while True:
  try:
    rg = int(input('digite o seu rg'))
    return rg
  except ValueError:
    print('insira um numero valido')

def cadastrar_pessoa(conn,cursor):
   while True:
    al=solicitar_rg()
    cursor.execute("SELECT * FROM alunos WHERE RG = ?",(al,))
    c=cursor.fetchone()
    if c is None:
      Dado_1=al
      break
    else:
      print('rg ja cadastrado')
  Dado_2=input('Qual seu nome? ')
  Dado_3=solicitar_idade()
  Dado_4=input('Qual seu genero ')
  pessoa_atual = (Dado_1,Dado_2,Dado_3,Dado_4,False,True)
  Registrar_Pessoa = ("INSERT INTO alunos (rg,name,age,gener,premium,adimp)VALUES(?, ? ,?, ?, ? ,?)")
  cursor.execute(Registrar_Pessoa,pessoa_atual)
  conn.commit()

def cadastrar_premium(conn,cursor):
    while True:
     al=solicitar_rg()
     cursor.execute("SELECT * FROM alunos WHERE RG = ?",(al,))
     c=cursor.fetchone()
     if c is None:
       Dado_1=al
       break
     else:
       print('rg ja cadastrado')
    Dado_2=input('Qual seu nome? ')
    Dado_3=solicitar_idade()
    Dado_4=input('Qual seu genero ')
    pessoa_atual = (Dado_1,Dado_2,Dado_3,Dado_4,True,True)
    Registrar_Pessoa = ("INSERT INTO alunos (rg,name,age,gener,premium,adimp)VALUES(?, ? ,?, ?, ? ,?)")
    cursor.execute(Registrar_Pessoa,pessoa_atual)
    conn.commit()

def consultar_ficha(cursor):
   while True:
    al=solicitar_rg()
    cursor.execute("SELECT * FROM alunos WHERE RG = ?",(al,))
    c=cursor.fetchone()
    if c is None:
     print('Rg nao cadastrado')
    else:
     Mostrar_dados(c[0],c[1],c[2],c[3],c[4],c[5])
     break

def Mostrar_dados(a,b,c,d,e,f):
    if f :
     h='Sim'
    else:
     h='Não'
    if e:
     print(f'RG : {a}\nNome : {b}\nIdade : {c}\nGenero : {d}\nPremium : Sim \n----------aluno premium----------')
    else:
     print(f'RG : {a}\nNome : {b}\nIdade : {c}\nGenero : {d}\nPremium : Não \n adimplente : {h}')

def registrar_pagamento(conn,cursor):
   al1,var,apt=validar_rg(cursor)
   if apt:
    print(f'o aluno : {al1} e premium e nao paga mensalidade')
   else:
    cursor.execute("UPDATE alunos SET adimp = 1 WHERE RG =?",(var,))
    conn.commit()
    print(f'pagamento do aluno : {al1} registrado com sucesso')

def listar_alunos(cursor):
    cursor.execute("SELECT * FROM alunos")
    e=cursor.fetchall()
    for f in e:
      Mostrar_dados(f[0],f[1],f[2],f[3],f[4],f[5])



def validar_rg(cursor):
 while True:
  val=solicitar_rg()
  cursor.execute("SELECT * FROM alunos WHERE RG = ?",(val,))
  d=cursor.fetchone()
  if d is None:
    print('rg nao cadastrado na base de dados')
  else:
    return(d[1],d[0],d[4])


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

def Banco_de_dados():
  import sqlite3
  conn = sqlite3.connect('curso.db')
  cursor= conn.cursor()
  create_table="""
  CREATE TABLE IF NOT EXISTS alunos(
  rg INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, gener TEXT NOT NULL, premium BOOLEAN NOT NULL, adimp BOOLEAN NOT NULL)"""
  cursor.execute(create_table)
  conn.commit()
  return conn, cursor

def Fechar_banco(conn):
  conn.close()

def Main():
 aberto=True
 conn,cursor=Banco_de_dados()
 while(aberto):
  mostrar_menu()
  opcao=Solicitar_opcao()
  if opcao == 1:
   cadastrar_pessoa(conn,cursor)
  elif opcao == 2:
    consultar_ficha(cursor)
  elif opcao == 3:
    registrar_pagamento(conn,cursor)
  elif opcao == 4:
    listar_alunos(cursor)
  elif opcao == 5:
    cadastrar_premium(conn,cursor)
  elif opcao == 6:
    Fechar_banco(conn)
    aberto = False
  else:
    print('por favor, tente uma opção valida')

Main()