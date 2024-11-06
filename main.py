from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configurações do WebDriver
chrome_options = Options()
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

def ler_dados_login(caminho_arquivo = 'usernames.xml'):
    # Verifica a extensão do arquivo
    if caminho_arquivo.endswith('.csv'):
        df = pd.read_csv('usernames.xml')
    elif caminho_arquivo.endswith('usernames.xml'):
        df = pd.read_xml('usernames.xml')
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv ou .xml.")
    
    # Extrai as informações necessárias
    return df.iloc[0]['Login'], df.iloc[0]['Senha']

def ler_dados_usuario(caminho_arquivo2 ='checkout.xml'):
    #Verifica a extensão do arquivo 2
    if caminho_arquivo2.endswith('.csv'):
        df = pd.read_csv('checkout.xml')
    elif caminho_arquivo2.endswith('checkout.xml'):
        df = pd.read_xml('checkout.xml')
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv ou .xml.")

    return df.iloc[0]['name'], df.iloc[0]['lastname'], df.iloc[0]['codigopostal']
    

def fazer_login(navegador, url, login, senha):
    # Navegar para o site
    navegador.get('https://www.saucedemo.com/v1/index.html')
    
    # Encontrar e preencher os campos de login
    campo_login = navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/form/input[1]')
    campo_login.send_keys(login)
    time.sleep(2)
    
    campo_senha =navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/form/input[2]')
    campo_senha.send_keys(senha)
    time.sleep(2)
    
    # Submeter o formulário de login
    botao_login = navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/form/input[3]')
    botao_login.click()

def adicionar_itens_ao_carrinho(navegador):
    # Adicionar um item ao carrinho
    item = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[6]/div[3]/button')
    item.click()
    time.sleep(2)  # Aguarda o item ser adicionado
    item = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/button')
    item.click()
    time.sleep(2)
    item = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button')
    item.click()
    time.sleep(2)


def visualizar_carrinho(navegador):
    # Ir para o carrinho
    botao_carrinho = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/a')
    botao_carrinho.click()
    time.sleep(2) 
    botao_checkout = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/a[2]')
    botao_checkout.click()
    time.sleep(2)

def checkout_informacoes(navegador, name, lastname, codigopostal):
    #Validar as ultimas informações pessoais
    campo_name = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[1]/input[1]')
    campo_name.send_keys(name)
    time.sleep(2)
    campo_lastname = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[1]/input[2]')
    campo_lastname.send_keys(lastname)
    time.sleep(2)
    campo_codigopostal = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[1]/input[3]')
    campo_codigopostal.send_keys(codigopostal)
    time.sleep(2)
    botao_continue = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[2]/input')
    botao_continue.click()

def validar_valor_final(navegador):
    #Define o valor total que possui no carrinho
    valor_total = navegador.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]').text
    print(f'O valor total do carrinho é {valor_total}')







def executar_automacao():
    # Caminho para o arquivo de login e senha
    caminho_arquivo = 'usernames.xml'
    #Caminho para o arquivo que contém as informações para checkout
    caminho_arquivo2 = 'checkout.xml'
    
    # URL do site
    url_site = 'https://www.saucedemo.com/v1/index.html'
    
    # Ler as credenciais do arquivo
    login, senha = ler_dados_login(caminho_arquivo)
    
    # Realizar login
    fazer_login(navegador, url_site, login, senha)
    
    # Adicionar itens ao carrinho
    adicionar_itens_ao_carrinho(navegador)

    #Visualizar carrinho
    visualizar_carrinho(navegador)

    #Validar as ultimas informações pessoais
    name, lastname, codigopostal = ler_dados_usuario(caminho_arquivo2)
    checkout_informacoes(navegador, name, lastname, codigopostal)

    # Localizar o elemento que contém o valor total do carrinho
    validar_valor_final(navegador)

    # Fechar o navegador
    navegador.quit()

    

if __name__ == "__main__":
    executar_automacao()
