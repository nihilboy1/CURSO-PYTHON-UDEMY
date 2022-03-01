from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

raiz = Path(__file__).parent
chromedriverlocal = raiz / 'chromedriver.exe'


# options.add_argument('--headless') --- com essa option o navegador n abre
# options.add_argument('window-size=400,800') ---
# com essa option eu delimito o tamanho da tela que será usada para utilização

def browser(*options: str) -> webdriver.Chrome:
    # criando opções
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
            # criando o serviço
    servix = ChromeService(executable_path=chromedriverlocal)
    # criando o driver
    driver = webdriver.Chrome(service=servix, options=chrome_options)
    return driver


digitador = browser()
digitador.get()

# O CÓDIGO BOM TA NO VSCODE
