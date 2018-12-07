# DesafioPiratasDeDados

Exercicio
Extrair dados de um site e gravar os resultados em um arquivo.

Introdução
Apresentar dados do site dos correios com  pelo menos dois estados.
Para cada estado, capturar 100 registros.
Cada registro deve conter uma "localidade" e uma "faixa de cep"
O formato de saída é JSONL

Instalação

- Editor de texto Gedit
- Navegador web (Firefox, Chrome)
- Instalar o python

Recursos para execução

- Importar as bibliotecas, request para acesso cliente http e BeautifulSoup para estruturar o conteúdo da página.

import requests

from bs4 import BeautifulSoup

//esta variavel passa como parametro a url onde será retirado a primeira parte dos dados
url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'

// variável que retira as informações da url
r = requests.get(url)

// variável que organiza a estrutura no formato da biblioteca BeautifulSoup
soup = BeautifulSoup(r.text, 'html5lib')

// variavel que armazena as informações contidas na função find da biblioteca BeautifulSoup
lista_tabela = soup.find_all('table',class_='tmptabela')
(entendo que aqui teríamos todas as informações contidas nas duas tabelas que 
aparecem na página, mas não foi o que consegui, por problemas técnicos)

//localizar todos os elementos cuja a tag o nome é "<td>" no inspecionar.
lista_tabela1 = lista_tabela.find_all('td') 
(pelo menos era isso que eu imaginei que faria mas não aconteceu isso, além disso depois eu ainda teria que filtrar
as informações da tag "td")

//fazer um loop pra cada lista_tabela1 
for lista_td in lista_tabela1: 

//a tag do horarios é "td" e extrair o texto
localidade = lista_tabela.find('td').text 
faixa = lista_tabela.find('td').text 

//criar uma lita e armazenar localidade e faixa de cep
dados.append((localidade,faixa))

depois teríamos que salvar no formato JSONL, como não consegui fazer o código funcionar, por falta de habilidade e experiência 
nesse tipo de ferramentas não criei o arquivo de saída

- Resultado: Caso executado, o procedimento seria repetidamente aproxidamente 4 vezes e os arquivos de 
saída concatenados 
