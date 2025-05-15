from datetime import date
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
    print("<---------------------->")

    try:
      opc = int(input())
    except Exception as erro:
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
        except:
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
        print("[1] -> Alimentação")
        print("[2] -> Combustível")
        print("<------------------------->")

        try:
          opc_gasto = int(input())
        except Exception as erro:
          opc_gasto = 10
        
        if opc_gasto == 0:
          print("Retornando ao Menu...")
          break
        elif opc_gasto == 1:
          pass
        elif opc_gasto == 2:
          pass
        else:
          print("Opção Inválida, por favor, selecione uma opção correta")

    else:
      print("Opção Inválida, por favor, selecione uma opção correta")