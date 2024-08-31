# sistema bancario do Bank ALL
menu = """ 
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair 
 """

saldo = 0
limit = 1000
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while(True):
    opcao = str(input(menu))
    # Depósito
    if opcao == 'd':
        valor = float(input('informe o valor de deposito :'))
        if valor > 0 : 
            saldo += valor 
            print('voce esta depositando')
            extrato = (f'Deposito: R$ {valor:.2f}\n')
        else:
            print('[ERRO] valor informado invalido')
    # Saque
    elif opcao == 's':
       valor = float(input('informe o valor de saque :'))
       if valor > 0:
         saldo -= valor
         extrato += (f" Saque: R$ {valor:.2f}\n")
         numero_saques += 1
         
         excedeu_saldo = valor > saldo
         excedeu_limite = valor> limit
         excedeu_saques = numero_saques >= LIMITE_SAQUES

         if excedeu_saldo:
             print('Operação falhou você não tem saldo o suficiente')
         elif excedeu_limite:
             print('operação falhou o valor do saque maior que o limite')
         elif excedeu_saques:  
             print('Operção falhou numero de saques excedidos')
         else:
             print('operação falhou valor informado invalido')
    # Extrato
    elif opcao == 'e':
        print('\n ========EXTRATO========')
        print('não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nsaldo: R$ {valor:.2f}')
        print('==========================')
    # Stop
    elif opcao ==  'q':
        print('saindo')
        break
    else: 
        print('[ERRO] Opção invalida')
