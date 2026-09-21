
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
    return e

def alterar_dados(cursor,conn,nome,idade,genero,premium,adimp,rg):
   cursor.execute("UPDATE alunos SET name = ?, age= ?, gener = ?, premium = ?, adimp = ? WHERE RG=?",(nome,idade,genero,premium,adimp,rg))
   conn.commit()
   return True

def validar_rg(cursor, rg):
    cursor.execute("SELECT * FROM alunos WHERE RG = ?", (rg,))
    d = cursor.fetchone()

    if d is None:
        return False, None, None
    else:
        return True, d[1], d[4]

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
def deletar(conn,cursor,rg):
   cursor.execute("DELETE FROM alunos WHERE RG = ?", (rg,))
   conn.commit()
   return True
def Main():
 aberto=True
 conn,cursor=Banco_de_dados()
if __name__ == "__main__":
    Main()