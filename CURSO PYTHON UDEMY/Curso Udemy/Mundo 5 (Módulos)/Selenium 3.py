from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Chromeauto:
    cpf = '713.343.270-68'
    produtotext = 'novo'
    conveniotext = 'inss'
    nome = 'samuel seve'
    ddd = '84'
    tel = '987055995'
    uf = 'rn'
    benef = '1840907883'

    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\User\samue\AppData\Local\Google\Chrome\User Data\Pessoa 1')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def acessa(self, link):
        self.chrome.get(link)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            guarda_login = self.chrome.find_element(By.XPATH, '//*[@id="txtUsuario"]')
            guarda_senha = self.chrome.find_element(By.XPATH, '//*[@id="txtSenha"]')
            guarda_login.send_keys('CBSU105591')
            guarda_senha.send_keys('Aburame@145')
            btn_entrar = self.chrome.find_element(By.XPATH, '//*[@id="btnEntrar"]')
            btn_entrar.click()
            sleep(0.7)
        except Exception as Erro:
            print(f'Erro ao tentar logar! {Erro}')

    def clica_painel(self):
        try:
            btn_msg = self.chrome.find_element(By.XPATH, '//*[@id="toast-container"]')
            if btn_msg:
                btn_msg.click()
            btn_painel = self.chrome.find_element(By.LINK_TEXT, 'Painel Controle')
            btn_painel.click()
        except Exception as Erro:
            print(f'Erro ao tentar clicar no painel! {Erro}')

    def novaprop(self):
        try:
            btn_prop = self.chrome.find_element(By.XPATH, '//*[@id="PainelControle_novaProposta"]/span')
            btn_prop.click()
            sleep(0.5)
        except Exception as Erro:
            print(f'Erro ao tentar clicar em nova proposta! {Erro}')

    def agente(self):
        try:
            btn_agente = self.chrome.find_element(By.XPATH, '//*[@id="txtAgenteCertificado"]')
            btn_agente.click()
            btn_agente.send_keys('12454722402')
            sleep(0.7)
            btn_agente2 = self.chrome.find_element(By.XPATH, '//*[@id="ui-id-1"]')
            btn_agente2.click()
            sleep(0.5)
            btn_pross = self.chrome.find_element(By.XPATH, '//*[@id="btnProsseguir"]/span')
            btn_pross.click()
            sleep(1)

        except Exception as Erro:
            print(f'Erro no agente! {Erro}')

    def tabela1(self):
        convenio = self.chrome.find_element(By.XPATH, '//*[@id="ddlConvenio_chzn"]/a/span')
        convenio.click()
        conveniotext = self.chrome.find_element(By.XPATH, '//*[@id="ddlConvenio_chzn"]/div/div/input')
        conveniotext.send_keys(Chromeauto.conveniotext)
        conveniotext.send_keys(Keys.ENTER)
        sleep(0.5)
        produto = self.chrome.find_element(By.XPATH, '//*[@id="ddlProduto_chzn"]/a/span')
        produto.click()
        produtotext = self.chrome.find_element(By.XPATH, '//*[@id="ddlProduto_chzn"]/div/div/input')
        produtotext.send_keys(Chromeauto.produtotext)
        produtotext.send_keys(Keys.ENTER)
        sleep(0.5)
        cpf = self.chrome.find_element(By.XPATH, '//*[@id="txtCPF"]')
        cpf.click()
        cpf.send_keys(Chromeauto.cpf)
        sleep(0.5)
        nome = self.chrome.find_element(By.XPATH, '//*[@id="txtNome"]')
        nome.click()
        nome.send_keys(Chromeauto.nome)
        nome.send_keys(Keys.TAB)
        sleep(0.5)
        form = self.chrome.find_element(By.XPATH, '//*[@id="ddlTipoFormalizacao_chzn"]/a/span')
        form.click()


if __name__ == '__main__':
    # Chromeauto.cpf = input('Informe o cpf do cliente: ')
    # Chromeauto.conveniotext = input('Informe o convenio: ')
    # Chromeauto.produtotext = input('Informe o produto: ')
    chrome = Chromeauto()
    chrome.acessa('https://epfweb.safra.com.br/Home/Login')
    chrome.faz_login()
    chrome.clica_painel()
    chrome.novaprop()
    chrome.agente()
    chrome.tabela1()
    sleep(10)
    chrome.sair()

# O CÓDIGO BOM TA NO VSCODE

