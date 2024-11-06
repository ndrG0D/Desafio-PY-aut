# Automação Web com Selenium em Python

Este projeto é uma automação simples em Python usando Selenium para interagir com um site específico, realizar login, adicionar itens ao carrinho, visualizar o carrinho e exibir o valor total da compra.

## Requisitos

- **Python 3.12**
- **Bibliotecas**: Selenium, Pandas, Webdriver Manager

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/ndrG0D/Desafio-PY-aut
   cd Desafio-PY-aut
2. Instale as dependências
    ```bash
    pip install selenium pandas webdriver-manager

**Uso**

1. Coloque os arquivos usernames.xml e checkout.xml no diretório do projeto.
2. Execute o script:
   ```bash
   python main.py
 **Funcionalidades**
- Leitura de dados: As credenciais de login e informações de checkout são lidas de arquivos .csv ou .xml.
  
**Ações automatizadas:**
 - Login no site.
 - Adição de itens ao carrinho.
 - Visualização do carrinho e processo de checkout.
 - Impressão do valor total da compra.
**Saída Esperada**
- O valor total do carrinho será impresso no terminal:

  ```bash
  O valor total do carrinho é Total: $45.33

(É esperado esse valor no output)

**Observações**
 - Verifique se o ChromeDriver é compatível com sua versão do Chrome.
 - Personalize os seletores XPath caso o site seja atualizado.

**Desenvolvido por André Victor**
