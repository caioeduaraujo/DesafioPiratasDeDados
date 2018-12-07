import requests
from bs4 import BeautifulSoup
url='http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')
lista_tabela = soup.find_all('table',class_='tmptabela')
lista_tabela1 = lista_tabela.find_all('td')
for lista_td in lista_tabela1:
localidade = lista_tabela.find('td').text 
faixa = lista_tabela.find('td').text
dados.append((localidade,faixa))
