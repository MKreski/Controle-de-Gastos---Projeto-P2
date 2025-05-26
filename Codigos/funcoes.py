from datetime import *
import unicodedata
mes_atual = date.month
ano_atual = date.year

def log(onde : str, erro : str):
    with open("../arquivos/log.txt", "a+") as arq:
        arq.write( "ocorreu um erro em - " + onde + " - erro: " + str(erro) + ". As " + str(datetime.now()) + "\n")

def get_from_dia():
    pass

def get_from_mes():
    pass

def get_from_ano(ano_pesquisa):
    pesquisa = []
    with open("../arquivos/gastos.txt", "r") as arq:
        for i in arq:
            gasto = i.strip().split(", ")
            data = gasto[3].split("/")
            if int(data[2]) == ano_pesquisa:
                pesquisa.append(i.strip())

    return pesquisa

def cadastro_tipos(tipo : str):
    texto_normalizado = unicodedata.normalize('NFKD', tipo)
    texto_sem_acentos = texto_normalizado.encode('ascii', 'ignore').decode('utf-8')
    frase = texto_sem_acentos
    with open("../arquivos/tipos.txt", "a+") as arq:
        arq.write(frase.upper() + "\n")

def mostrar_tipos():
    with open("../arquivos/tipos.txt", "r") as arq:
        for i in arq:
            print(i.strip())

def mostrar_tipos_menu():
    with open("../arquivos/tipos.txt", "r") as arq:
        for idx, tipo in enumerate(arq):
            print(f"[{idx + 1}] -> {tipo.strip()}")

def listar_tipos():
    tipos = []
    with open("../arquivos/tipos.txt", "r") as arq:
        for i in arq:
            tipos.append(i.strip())
    return tipos

def salvar_gasto(tipo : str, nome : str, valor : float, data : list):
    data_gasto = data[0] + "/" + data[1] + "/" + data[2]
    with open("../arquivos/gastos.txt", "a+") as arq:
        arq.write(f"{tipo}, {nome}, {valor}, {data_gasto}\n")