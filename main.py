
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

def cadastrar_pessoa(conn,cursor,rg,nome,idade,genero):
       cursor.execute("SELECT * FROM alunos WHERE RG = ?",(rg,))
       c=cursor.fetchone()
       if c is None:
        pessoa_atual = (rg,nome,idade,genero,False,True)
        Registrar_Pessoa = ("INSERT INTO alunos (rg,name,age,gener,premium,adimp)VALUES(?, ? ,?, ?, ? ,?)")
        cursor.execute(Registrar_Pessoa,pessoa_atual)
        conn.commit()
        return True
       else:
         return False

def cadastrar_premium(conn,cursor,rg,nome,idade,genero):
     cursor.execute("SELECT * FROM alunos WHERE RG = ?",(rg,))
     c=cursor.fetchone()
     if c is None:
      pessoa_atual = (rg,nome,idade,genero,True,True)
      Registrar_Pessoa = ("INSERT INTO alunos (rg,name,age,gener,premium,adimp)VALUES(?, ? ,?, ?, ? ,?)")
      cursor.execute(Registrar_Pessoa,pessoa_atual)
      conn.commit()
      return True
     else:
       return False

def consultar_ficha(cursor,rg):
    cursor.execute("SELECT * FROM alunos WHERE RG = ?",(rg,))
    c=cursor.fetchone()
    if c is None:
     return False,None,None,None,None,None,None
    else:
     return True,c[0],c[1],c[2],c[3],c[4],c[5]

def Mostrar_dados(a,b,c,d,e,f):
    if f :
     h='Sim'
    else:
     h='Não'
    if e:
     print(f'RG : {a}\nNome : {b}\nIdade : {c}\nGenero : {d}\nPremium : Sim \n----------aluno premium----------')
    else:
     print(f'RG : {a}\nNome : {b}\nIdade : {c}\nGenero : {d}\nPremium : Não \n adimplente : {h}')

def registrar_pagamento(conn, cursor, rg):
    existe, nome, premium = validar_rg(cursor, rg)

    if existe:
        if premium:
            return False, rg, nome, True
        else:
            cursor.execute(
                "UPDATE alunos SET adimp = 1 WHERE RG = ?",
                (rg,)
            )
            conn.commit()
            return True, rg, nome, True
    else:
        return False, None, None, False
    
def listar_alunos(cursor):
    cursor.execute("SELECT * FROM alunos")
    e=cursor.fetchall()
    for f in e:
      Mostrar_dados(f[0],f[1],f[2],f[3],f[4],f[5])



def validar_rg(cursor, rg):
    cursor.execute("SELECT * FROM alunos WHERE RG = ?", (rg,))
    d = cursor.fetchone()

    if d is None:
        return False, None, None
    else:
        return True, d[1], d[4]

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
  if opcao == 3:
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
if __name__ == "__main__":
    Main()