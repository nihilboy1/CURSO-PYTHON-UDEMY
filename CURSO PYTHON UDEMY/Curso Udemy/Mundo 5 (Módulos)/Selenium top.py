from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

'''raiz = Path(__file__).parent
chromedriverlocal = raiz / 'chromedriver.exe'

'''


class Browser:
    def __init__(self, *options: str):
        raiz = Path(__file__).parent
        chromedriverlocal = raiz / 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)
        servix = ChromeService(executable_path=chromedriverlocal)
        self.driver = webdriver.Chrome(service=servix, options=chrome_options)


a = Browser('window-size=400,800')
a.driver.get('https://www.sinonimos.com.br/')
