import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

print("O download está prestes a começar ...")
page = requests.get(
    'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude')

soup = BeautifulSoup(page.text, 'html.parser')

anchor_tags_list = soup.select("p.callout>a")

zipObj = ZipFile('Anexos.zip', 'w') # opens a new a zip file in Write mode

for tag in anchor_tags_list: 
    href = tag.get('href') # gets the href content for every anchor tag
    file_name = href.split('/')[-1]  # gets the file name from the last index of the split operation
    if ("Anexo" in file_name) and (".pdf" in file_name): # searchs for Anexo and pdf format in file name
        file = requests.get(href)
        open(file_name, 'wb').write(file.content) # writes pdf tile to system
        zipObj.write(file_name) # writes downloaded pdf file to zip file previously created: see line 13

print("Download concluído!")
zipObj.close();
