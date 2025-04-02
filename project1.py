import os
from tkinter.filedialog import askdirectory
caminho = askdirectory (title='Selecione uma pasta') #Pergunta ao usuário qual o diretório que deve organizar

lista_arquivos = os.listdir(caminho) #Define lista_arquivos

# Cria um dicionário, definindo "nome da pasta": ["extensão"]
locais = { 
    "imagens": [".png", ".jpg"],
    "planilhas": [".csv"],
    "pdfs": [".pdf"],
}


for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}') #Splita o arquivo em nome e extensão
    for pasta in locais:
        if extensao in locais[pasta]: #Define que se a extensão está na pasta e o diretório não existe, crie (mkdir)
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
        