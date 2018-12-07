# DesafioPiratasDeDados

# Exercicio
Extrair dados de um site e gravar os resultados em um arquivo.

# Introdução
Apresentar dados do site dos correios com  pelo menos dois estados. Para cada estado, capturar 100 registros.
Cada registro deve conter uma "localidade" e uma "faixa de cep". Salvar em formato de saída JSONL.

# Instalação

- Editor de texto Gedit
- Navegador web (Firefox, Chrome)
- Instalar o python

# Recursos para execução

//Importar as bibliotecas, request para acesso cliente http e BeautifulSoup para estruturar o conteúdo da página.
import requests
from bs4 import BeautifulSoup

//esta variavel passa como parametro a url onde será retirado a primeira parte dos dados
url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'

// variável que retira as informações da url
r = requests.get(url)

// variável que organiza a estrutura no formato da biblioteca BeautifulSoup
soup = BeautifulSoup(r.text, 'html5lib')

// variavel que armazena as informações contidas na função "Find" da biblioteca BeautifulSoup
lista_tabela = soup.find_all('table',class_='tmptabela')
(Nesta etapa entendo que a variavel lista_tabela retornaria as informações de todas as tabelas denominadas
'tmptabela' inclusive uma destas conteria a localidade e faixa de cep)

Os comandos a seguir, infelizmente não consegui executar e rodar.
Através do conhecimento adquirido durante a realização da tarefa, segue abaixo uma possivel execução para finalizar o desafio.


//localizar todos os elementos cuja a tag é "<td>" no inspecionar(f12).
 lista_tabela1 = lista_tabela.find_all('td') 
(acredito que o passpo seguinte seria filtrar as informações de localidade e faixa de cep da tag "td")

  
//Loop pra cada lista_tabela1 
for lista_td in lista_tabela1: 

//a tag da faixa e da localidade são "td", os arquivos de saida tem o formato text
localidade = lista_tabela.find('td').text 
faixa = lista_tabela.find('td').text 

//Lista que armazena localidade e faixa de cep
dados.append((localidade,faixa))


- Resultado: Caso executado, o procedimento seria repetidamente aproxidamente 4 vezes e os arquivos de 
saída concatenados 


Para finalização do desafio salvar no formato JSONL, infelizmente não executei o código.
