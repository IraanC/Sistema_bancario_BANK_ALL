# sistema bancario do Bank ALL
menu = """ 
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair 
=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 500

while(True):
    opcao = float(input(menu))
    if opcao == 'd':
        valor = input('informe o valor de deposito :')
        if valor > 0 : 
            saldo += valor 
            extrato = f'Deposito: R$ {valor:.2f}\n'
        else:
            print('[ERRO] valor informado invalido')

    if opcao == 's':
       valor = float(input('informe o valor de saque :'))

       excedeu_saldo = valor > saldo
       excedeu_limite = valor> limite
       excedeu_saques = numero_saques >= LIMITE_SAQUES

       if excedeu_saldo:
           print('Operação falhou você não tem saldo o suficiente')
       elif excedeu_limite:
           print('operação falhou o valor do saque maior que o limite')
       elif excedeu_saques:
           print('Operção falhou numero de saques excedidos')
       elif valor > 0:
           saldo -= valor
           extrato += f" Saque: R$ {valor:.2f}\n"
           numero_saques += 1
       else:
           print('operação falhou valor informado invalido')

    if opcao == 'e':
        print('\n ========EXTRATO========')
        print('não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nsaldo: R$ {valor:.2f}')
        print('==========================')
    if opcao ==  'q':
        print('saindo')
        break
    else: 
        print('[ERRO] operação invalida')
