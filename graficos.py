import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import main
def Grafico_de_idades(cursor):
   dados=main.listar_alunos(cursor)
   df_todas=pd.DataFrame(dados,columns=["Rg",'Nome',"Idade","Genero","Premium","Adimplente"])
   idade=df_todas["Idade"].value_counts()
   fig,ax=plt.subplots(figsize=(5,5))
   ax.pie(idade.values,labels=idade.index)
   return fig


def Grafico_geral(cursor):
 dados=main.listar_alunos(cursor)
 df_todas=pd.DataFrame(dados,columns=["Rg",'Nome',"Idade","Genero","Premium","Adimplente"])
 return df_todas


def Grafico_de_adimplencia(cursor):
   dados=main.listar_alunos(cursor)
   df_todas=pd.DataFrame(dados,columns=["Rg",'Nome',"Idade","Genero","Premium","Adimplente"])
   adimplencia=df_todas["Adimplente"].value_counts()
   labels = ["Adimplente" if valor == 1 else "Inadimplente"for valor in adimplencia.index]
   fig, ax = plt.subplots(figsize=(5, 5))
   ax.bar(labels, adimplencia.values)
   return fig



def Grafico_de_generos(cursor):
   dados=main.listar_alunos(cursor)
   df_todas=pd.DataFrame(dados,columns=["Rg",'Nome',"Idade","Genero","Premium","Adimplente"])
   genero=df_todas["Genero"].value_counts()
   fig, ax = plt.subplots(figsize=(6,5))
   ax.pie(genero.values,labels=genero.index)
   return fig