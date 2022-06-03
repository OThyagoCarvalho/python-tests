import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

print("O download está prestes a começar ...")
page = requests.get(
    'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude')

soup = BeautifulSoup(page.text, 'html.parser')

anchor_tags_list = soup.select("p.callout>a")

zipObj = ZipFile('Anexos.zip', 'w')

for tag in anchor_tags_list:
    href = tag.get('href')
    file_name = href.split('/')[-1]
    if ("Anexo" in file_name) and (".pdf" in file_name):
        file = requests.get(href)
        open(file_name, 'wb').write(file.content)
        zipObj.write(file_name)
