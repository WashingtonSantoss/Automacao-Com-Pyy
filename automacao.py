#Aula 1 do Projeto Python // Automatizar Cadastro de Produtos //


import pyautogui
import time
import pandas
# pyautogui -> Fazer automações com python
#pyautogui.press PRESSIONA UMA TECLA
#pyautogui.write ESCREVE
#pyautogui.click CLICA

pyautogui.PAUSE = 0.5

#Passo 1: Entrar no sistema da empresa -- https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Chrome e digitar o site que eu quero entrar
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#Passo 2: Fazer login
pyautogui.click(x=867, y=377)
pyautogui.write("washinsantos907@gmail.com")
pyautogui.press("tab")
pyautogui.write("5800123Was@")
pyautogui.press("enter")
time.sleep(2)

#Passo 3: importar a base de dados

tabela = pandas.read_csv('Aula1/produtos.csv')

#Passo 4: Cadastrar 1 produto
'''time.sleep(1)
pyautogui.click(x=866, y=256)
codigo = "MOLO00251"
marca = "Logitech"
tipo = "Mouse"
categoria = "1"
preco_unitario = "25.95"
custo = "6.50"
obs = ""

pyautogui.write(codigo)
pyautogui.press("tab")
pyautogui.write(marca)
pyautogui.press("tab")
pyautogui.write(tipo)
pyautogui.press("tab")
pyautogui.write(categoria)
pyautogui.press("tab")
pyautogui.write(preco_unitario)
pyautogui.press("tab")
pyautogui.write(custo)
pyautogui.press("tab")
pyautogui.write(obs)
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 5: Repetir para todos os produtos
pyautogui.scroll(10000)'''

#Passo 5: Cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=866, y=256)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")


    obs = tabela.loc[linha, "obs"]
    if obs != "non":
        pyautogui.write("None")
    


    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(10000)

    
    
    
    
    
    
    
    
    


