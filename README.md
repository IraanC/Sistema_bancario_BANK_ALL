
---

# Documentação do Sistema Bancário do Bank ALL

## Visão Geral

O sistema bancário do Bank ALL é um aplicativo simples de gerenciamento financeiro que permite realizar depósitos, saques e consultar o extrato da conta. O sistema também possui limitações para saques e fornece mensagens de erro apropriadas para operações inválidas.

## Menu de Opções

O menu principal do sistema apresenta as seguintes opções:

- **[d] Depositar**: Realiza um depósito na conta.
- **[s] Sacar**: Realiza um saque da conta.
- **[e] Extrato**: Exibe o extrato das operações realizadas.
- **[q] Sair**: Encerra o programa.

## Variáveis e Limites

- **saldo**: Representa o saldo atual da conta. Inicialmente é definido como 0.
- **limit**: Representa o limite máximo permitido para um saque. Inicialmente é definido como 1000.
- **extrato**: Armazena o histórico de transações realizadas (depósitos e saques). Inicialmente é uma string vazia.
- **numero_saques**: Conta o número de saques realizados. Inicialmente é definido como 0.
- **LIMITE_SAQUES**: Define o número máximo de saques permitidos por período. Inicialmente é definido como 3.

## Funcionalidades

### 1. Depósito (`d`)

- **Descrição**: Permite que o usuário deposite um valor na conta.
- **Entrada**: Valor do depósito (deve ser um número positivo).
- **Processo**: Adiciona o valor ao saldo e registra a transação no extrato.
- **Mensagens**:
  - Se o valor for positivo, a transação é realizada com sucesso e uma mensagem de confirmação é exibida.
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
  - "Operação falhou: você não tem saldo suficiente."
  - "Operação falhou: o valor do saque é maior que o limite."
  - "Operação falhou: número de saques excedido."
  - "Operação falhou: valor informado inválido."

### 3. Extrato (`e`)

- **Descrição**: Exibe o extrato das transações realizadas.
- **Processo**: Mostra todas as movimentações realizadas e o saldo atual.
- **Mensagens**:
  - Se não houver transações, exibe uma mensagem indicando que não foram realizadas movimentações.
  - Exibe o saldo atual da conta.

### 4. Sair (`q`)

- **Descrição**: Encerra o programa.
- **Processo**: Imprime uma mensagem de saída e encerra o loop do programa.

## Tratamento de Erros

- **Opção inválida**: Quando o usuário insere uma opção que não está no menu, uma mensagem de erro é exibida indicando que a opção é inválida.

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
   - O sistema verifica o saldo, limite e número de saques.
   - Se qualquer condição falhar, uma mensagem de erro é exibida.

3. **Extrato**:
   - Usuário escolhe `e`.
   - O sistema exibe todas as transações e o saldo atual.

4. **Sair**:
   - Usuário escolhe `q`.
   - O sistema imprime uma mensagem de saída e encerra o programa.

---

Esta documentação cobre as principais funcionalidades e regras do sistema bancário do Bank ALL. Se houver mais requisitos ou alterações, ajuste a documentação conforme necessário.
