import pyautogui as gui
import time
import pandas

gui.PAUSE = 1
gui.press('win')
gui.write('opera')
gui.press('enter')
time.sleep(4)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
gui.write(link)
gui.press('enter')
time.sleep(6)
gui.click(x=447, y=390)

gui.write('teste@gmail.com')
gui.press('tab')
gui.write('1234')
gui.press('tab')
gui.press('enter')

time.sleep(2)
tabela = pandas.read_csv("produtos.csv")

#cadastrando produtos
for linha in tabela.index:

    gui.click(x=543, y=273)
    gui.write(str(tabela.loc[linha, "codigo"]))
    gui.press('tab')
    gui.write(str(tabela.loc[linha, "marca"]))
    gui.press('tab')
    gui.write(str(tabela.loc[linha, "tipo"]))
    gui.press('tab')
    gui.write(str(tabela.loc[linha, "categoria"]))
    gui.press('tab')
    gui.write(str(tabela.loc[linha, "preco_unitario"]))
    gui.press('tab')
    gui.write(str(tabela.loc[linha, "custo"]))
    gui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        gui.write(str(obs))

    #apertar no enviar
    gui.press('tab')
    gui.press('enter')
    gui.scroll(5000)

