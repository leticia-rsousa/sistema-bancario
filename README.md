## Sistema Bancário
**Descrição Geral** 📄<br>
Este projeto apresenta uma **aplicação de sistema bancário digital**, desenvolvida em **Python** utilizando **POO (Programação Orientada a Objetos)**. O sistema permite gerenciar **clientes, contas correntes e poupança**, realizar **depósitos, saques, extratos e vinculação de contas aos clientes**, e demonstra conceitos de **herança, polimorfismo, encapsulamento e tratamento de exceções** em aplicações reais.

---
**Objetivo** 🎯 <br> 
O objetivo principal do projeto é fornecer uma **simulação completa de operações bancárias**, organizando clientes e contas, permitindo a execução de transações e explorando boas práticas de **POO e estrutura de software modular**.

---
**Tecnologias Utilizadas** 💻 <br>
* ***Python*** - linguagem principal.
* ***POO (Classes, Herança, Polimorfismo, Encapsulamento)*** - estrutura do sistema.
* ***Módulos e Pacotes Python*** - organização em pastas e arquivos.
* ***Tratamento de Exceções Personalizadas*** - para saldo insuficiente e contas inexistentes.

---
**Arquitetura e Estrutura do Código** 🧱 <br><br>
***1. Pasta Entidades*** <br>
Responsável por definir as classes do modelo de dados:
* ***Cliente.py*** – Representa os clientes e associa contas.
* ***Conta.py*** – Define a classe abstrata Conta e suas subclasses ContaCorrente e ContaPoupança, incluindo métodos de saque, depósito e extrato.

***2. Pasta Operacoes*** <br>
Responsável por gerenciar operações bancárias:
* ***Banco.py*** – Classe principal que gerencia clientes, contas e vinculação entre eles.

***3. Pasta Utilitarios*** <br>
Contém exceções personalizadas usadas na aplicação:
* ***exceptions.py*** – Exceções para saldo insuficiente e contas inexistentes.

***4. Script Principal (Sistema_Bancario.py)*** <br>
Responsável por:
* ***Executar o menu principal e menus de operações das contas.***
* ***Receber input do usuário para adicionar clientes, criar contas, realizar depósitos, saques e exibir extratos.***
* ***Demonstrar o fluxo de interação com as classes e tratamento de exceções.***

---
**Conceitos e Funcionalidades Demonstradas** 🔍 <br><br>
✅ ***Programação Orientada a Objetos:*** <br>
Uso de **classes, herança, polimorfismo e encapsulamento** para modelar clientes e contas.

✅***Tratamento de exceções:*** <br>
Validação de operações financeiras, como **saques acima do saldo ou contas inexistentes**.

✅***Organização modular:*** <br>
Separação do sistema em **Entidades, Operações e Utilitários**, seguindo boas práticas de estrutura de código.

✅***Fluxo interativo:*** <br>
Menus no terminal para interação com o sistema bancário, permitindo testar funcionalidades como **depósitos, saques e extratos**.

---
**Como Executar o Projeto** ▶️ <br><br>
***1. Execute o script principal:*** <br>
```Sistema_Bancario.py```

***2. Siga as instruções no terminal para navegar pelos menus e operações do banco.*** <br>

***Exemplo de Uso:*** <br>
```
Menu Principal:
1. Adicionar Cliente
2. Criar Conta
3. Acessar Conta
4. Sair

Escolha uma opção: 1
Digite o nome do cliente: João Silva
Digite o CPF do cliente: 12345678900
Cliente João Silva adicionado com sucesso!

Escolha uma opção: 2
Digite o CPF do cliente para vincular a conta: 12345678900
Digite o tipo da conta (corrente/poupanca): corrente
Conta corrente n° 1 criada para o cliente João Silva.
```

---
**Conclusão** 📌 <br>
Este projeto demonstra como criar uma **aplicação bancária completa em Python**, utilizando conceitos de **POO, modularidade, tratamento de exceções e interação com o usuário**. Ele serve como exemplo de **organização de código, estrutura de classes e desenvolvimento de sistemas interativos para gerenciamento financeiro.**
