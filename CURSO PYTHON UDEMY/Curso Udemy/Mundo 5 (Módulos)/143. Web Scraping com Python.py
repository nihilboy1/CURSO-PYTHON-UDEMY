import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
for perguntas in html.select('.mln24'):
    titulo = perguntas.select_one('.question-hyperlink')
    vote = perguntas.select_one('.vote')
    time = perguntas.select_one('.user-action-time')
    print(titulo.text,vote.text,time.text, sep='\t')






