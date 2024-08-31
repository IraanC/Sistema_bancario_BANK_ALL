## Visão Geral

O sistema bancário do Bank ALL é uma aplicação simplificada para gerenciamento de contas bancárias fictícias. Ele permite realizar depósitos, saques e consultar extratos. O sistema tem um limite de saque e um número máximo de saques permitidos por período.

## Menu de Opções

O menu principal do sistema oferece as seguintes opções:

- **[d] Depositar**: Realizar um depósito na conta.
- **[s] Sacar**: Realizar um saque da conta.
- **[e] Extrato**: Exibir o extrato das transações realizadas.
- **[q] Sair**: Encerrar o programa.

## Variáveis e Limites

- **saldo**: Representa o saldo atual da conta. Inicialmente definido como 0.
- **limit**: Limite máximo permitido para um saque. Inicialmente definido como R$ 1000,00.
- **extrato**: Histórico das transações realizadas (depósitos e saques). Inicialmente uma string vazia.
- **numero_saques**: Contador de saques realizados. Inicialmente definido como 0.
- **LIMITE_SAQUES**: Número máximo de saques permitidos por período. Inicialmente definido como 3.

## Funcionalidades

### 1. Depósito (`d`)

- **Descrição**: Permite que o usuário deposite um valor na conta.
- **Entrada**: Valor do depósito (deve ser um número positivo).
- **Processo**: Adiciona o valor ao saldo e registra a transação no extrato.
- **Mensagens**:
  - Se o valor for positivo, a transação é realizada e uma mensagem de confirmação é exibida.
  - Se o valor for inválido (não positivo), uma mensagem de erro é exibida.

### 2. Saque (`s`)

- **Descrição**: Permite que o usuário saque um valor da conta.
- **Entrada**: Valor do saque (deve ser um número positivo).
- **Processo**:
  - Verifica se o valor do saque é maior que o saldo disponível.
  - Verifica se o valor do saque ultrapassa o limite permitido.
  - Verifica se o número máximo de saques foi atingido.
  - Se todas as condições forem satisfeitas, o saque é realizado e registrado no extrato. Caso contrário, uma mensagem de erro apropriada é exibida.
- **Mensagens de Erro**:
  - "Operação falhou: saldo insuficiente." - Se o valor do saque exceder o saldo disponível.
  - "Operação falhou: valor do saque maior que o limite permitido." - Se o valor do saque exceder o limite estabelecido.
  - "Operação falhou: número máximo de saques excedido." - Se o número de saques atingir o limite máximo.
  - "Operação falhou: valor informado inválido." - Se o valor informado for não positivo.

### 3. Extrato (`e`)

- **Descrição**: Exibe o extrato das transações realizadas.
- **Processo**: Mostra todas as movimentações realizadas e o saldo atual.
- **Mensagens**:
  - Se não houver transações, exibe a mensagem "Não foram realizadas movimentações."
  - Exibe o saldo atual da conta.

### 4. Sair (`q`)

- **Descrição**: Encerra o programa.
- **Processo**: Imprime uma mensagem de despedida e encerra o loop do programa.

## Tratamento de Erros

- **Opção Inválida**: Quando o usuário insere uma opção que não está no menu, o sistema exibe a mensagem "[ERRO] Opção inválida".

## Exemplo de Execução

```plaintext
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair 
```

1. **Depósito**:
   - Usuário escolhe `d`.
   - Sistema solicita o valor para depósito.
   - Se o valor for válido, o depósito é realizado e registrado.

2. **Saque**:
   - Usuário escolhe `s`.
   - Sistema solicita o valor para saque.
   - O sistema verifica saldo, limite e número de saques.
   - Se qualquer condição falhar, uma mensagem de erro é exibida.

3. **Extrato**:
   - Usuário escolhe `e`.
   - O sistema exibe todas as transações e o saldo atual.

4. **Sair**:
   - Usuário escolhe `q`.
   - O sistema imprime uma mensagem de saída e encerra o programa.

---

Esta documentação detalha o funcionamento e regras do sistema bancário fictício Bank ALL. Ajustes podem ser feitos conforme necessário para atender a requisitos adicionais ou alterações.
