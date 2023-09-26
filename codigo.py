import pyautogui as gui
import pandas as pd
import time


def cadastrar_produto(codigo, marca, tipo, categoria, preco_unitario, custo, obs):
    # Clica em coordenadas específicas para iniciar o cadastro de produtos
    gui.click(x=543, y=273)
    # Preenche os campos do formulário de cadastro
    gui.write(str(codigo))
    gui.press('tab')
    gui.write(str(marca))
    gui.press('tab')
    gui.write(str(tipo))
    gui.press('tab')
    gui.write(str(categoria))
    gui.press('tab')
    gui.write(str(preco_unitario))
    gui.press('tab')
    gui.write(str(custo))
    gui.press('tab')

    if not pd.isna(obs):
        # Preenche o campo de observações, se houver
        gui.write(str(obs))

    # Pressiona Tab e Enter para enviar o formulário
    gui.press('tab')
    gui.press('enter')
    # Realiza uma rolagem para baixo na página
    gui.scroll(5000)


class AutomacaoWeb:
    def __init__(self):
        # Configura o tempo de pausa entre ações
        gui.PAUSE = 1
        # Define a URL de login
        self.login_url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

    def fazer_login(self, email, senha):
        # Abre o menu Iniciar
        gui.press('win')
        # Digita "opera" para buscar o navegador Opera (certifique-se de que o Opera esteja instalado)
        gui.write('opera')
        # Pressiona Enter para abrir o Opera
        gui.press('enter')
        # Digita a URL de login
        gui.write(self.login_url)
        # Pressiona Enter para acessar a página de login
        gui.press('enter')
        # Define tempo de espera para página carregar
        time.sleep(4)
        # Clica em coordenadas específicas para selecionar o campo de email
        gui.click(x=447, y=390)
        # Digita o email
        gui.write(email)
        # Pressiona Tab para ir para o campo de senha
        gui.press('tab')
        # Digita a senha
        gui.write(senha)
        # Pressiona Enter para fazer o login
        gui.press('tab')
        gui.press('enter')

    def automatizar(self, email, senha, csv_file):
        # Executa o processo de automação
        self.fazer_login(email, senha)
        # Lê o arquivo CSV com os dados dos produtos
        tabela = pd.read_csv(csv_file)

        # Itera sobre as linhas do CSV para cadastrar produtos
        for linha in tabela.index:
            cadastrar_produto(
                tabela.loc[linha, "codigo"],
                tabela.loc[linha, "marca"],
                tabela.loc[linha, "tipo"],
                tabela.loc[linha, "categoria"],
                tabela.loc[linha, "preco_unitario"],
                tabela.loc[linha, "custo"],
                tabela.loc[linha, "obs"]
            )


if __name__ == "__main__":
    automacao = AutomacaoWeb()
    # Inicia o processo de automação com email, senha e arquivo CSV
    automacao.automatizar('teste@gmail.com', '1234', 'produtos.csv')
