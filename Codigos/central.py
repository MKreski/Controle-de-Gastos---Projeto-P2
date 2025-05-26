from datetime import *
from funcoes import *
'''
Controle de Gastos - Até 03/06
-> Cadastro do Gasto (nome, valor, data, tipo)
  -> Cadastro de Tipo (alimentação, combustível)
  
-> Extrato por período(dia, mês, ano)
  -> Mostrar todos os dados do gasto do período selecionado
'''

print("Bem-vindo ao Controle de Gastos!")
while True:
    print("<-------->MENU<-------->")
    hoje = date.today()
    print(hoje.strftime("Hoje -- %d/%m/%y"))
    print("O que deseja fazer?")
    print("[0] -> SAIR")
    print("[1] -> Ver Extrato")
    print("[2] -> Adicionar Gasto")
    print("[3] -> Adicionar Tipo de Gasto")
    print("<---------------------->")

    try:
      opc = int(input())
    except Exception as erro:
      log("menu principal", erro)
      opc = 10

    if opc == 0:
      print("Obrigado pela atenção!")
      print("Saindo...")
      break

    elif opc == 1: #extrato
      while True:
        print("<-------->EXTRATO<-------->")
        print("Quer buscar o extrato por qual periodo?")
        print("[0] -> Voltar ao Menu")
        print("[1] -> Dia")
        print("[2] -> Mês")
        print("[3] -> Ano")
        print("<------------------------->")

        try:
          opc_extrato = int(input())
        except Exception as erro:
          log("periodo de gastos", erro)
          opc_extrato = 10

        if opc_extrato == 0:
          print("Retornando ao Menu...")
          break
        elif opc_extrato == 1:
          pass
        elif opc_extrato == 2:
          pass
        elif opc_extrato == 3:
          pass
        else:
          print("Opção Inválida, por favor, selecione uma opção correta")

    elif opc == 2: #adicionar gasto
      while True:
        print("<-------->ADICIONAR GASTO<-------->")
        print("Qual tipo de gasto a ser adicionado?")
        print("[0] -> Voltar ao Menu")
        mostrar_tipos_menu()
        print("<------------------------->")

        try:
          opc_gasto = int(input())
        except Exception as erro:
          log("adicionar gastos", erro)
          opc_gasto = 10
        
        if opc_gasto == 0:
          print("Retornando ao Menu...")
          break
        else:
          tipo_selecionado = ""
          for idx, tipo in enumerate(listar_tipos()):
            if opc_gasto == idx + 1:
              tipo_selecionado = tipo
          
          if tipo_selecionado == "":
            print("Tipo inválido, por favor, selecione um tipo válido")
            continue
          else:
            while True:
              print("Digite o nome do gasto:")
              nome = input()
              if nome == "":
                print("Nome inválido, por favor, digite um nome válido")
                continue
                
              print("Digite o valor do gasto:")
              try:
                valor = float(input())
              except Exception as erro:
                log("adicionar valor", erro)
                print("Valor inválido, por favor, digite um valor válido")
                continue
              
              print("Digite a data do gasto (dd/mm/aa):")
              try:
                data = input().split("/")
              except Exception as erro:
                log("adicionar data", erro)
                print("Data inválida, por favor, digite uma data válida")
                continue 

              print("Gasto a ser cadastrado:")
              print(f"Tipo: {tipo_selecionado}")
              print(f"Nome: {nome}")
              print(f"Valor: {valor}")
              print(f"Data: {data}")  

              try:
                salvar_gasto(tipo_selecionado, nome, valor, data)
                print("Gasto cadastrado com sucesso!")
              except Exception as erro:
                log("salvar gasto", erro)
                print("Erro ao salvar o gasto, por favor, tente novamente")
                continue
              
              break
              
    elif opc == 3: #adicionar tipo
      while True:
        print("<-------->ADICIONAR TIPO<-------->")
        print("O que deseja fazer?")
        print("[0] -> Voltar ao Menu")
        print("[1] -> Cadastro de Tipo")
        print("[2] -> Listar Tipos")
        print("<------------------------->")

        try:
          opc_tipo = int(input())
        except Exception as erro:
          log("adicionar tipos", erro)
          opc_tipo = 10

        if opc_tipo == 0:
          print("Retornando ao Menu...")
          break
        elif opc_tipo == 1:
          while True:
            print("Digite o nome do tipo de gasto:")
            tipo = input()
            if tipo == "":
              print("Tipo inválido, por favor, digite um tipo válido")
            else:
              break
          cadastro_tipos(tipo)
          print("Tipo cadastrado com sucesso!")
        elif opc_tipo == 2:
          print("<------------------------->")
          print("Tipos cadastrados:")
          mostrar_tipos()
          print("<------------------------->")

    else:
      print("Opção Inválida, por favor, selecione uma opção correta")