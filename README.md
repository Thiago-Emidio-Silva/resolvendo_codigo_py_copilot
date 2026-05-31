# 🐍 Resolvendo Código Python com Copilot - DESAFIO DIO.ME

Um repositório com exemplos de programas Python bem estruturados e comentados, desenvolvidos para fins educacionais.

---

## 📋 Sobre o Repositório

Este repositório contém três aplicações Python com finalidades diferentes, cada uma desenvolvida com:
- ✅ Código comentado e bem documentado
- ✅ Validações robustas de entrada
- ✅ Tratamento completo de exceções
- ✅ Interface amigável ao usuário
- ✅ Docstrings em todas as funções
- ✅ Boas práticas de programação

---

## 📁 Estrutura do Projeto

```
resolvendo_codigo_py_copilot/
│
├── README.md                    # Este arquivo
│
└── Code/
    ├── Concat_dados.py          # Concatenador de dados pessoais
    ├── repet_txt.py             # Repetidor de texto
    └── oper_mat.py              # Calculadora matemática
```

---

## 🚀 Programas Disponíveis

### 1️⃣ **Concat_dados.py** - Concatenador de Dados Pessoais

Um programa que coleta e organiza informações pessoais do usuário, com validação completa.

#### 📌 Funcionalidades:
- **Campos Obrigatórios:**
  - Nome (apenas letras e espaços)
  - Sobrenome (apenas letras e espaços)

- **Campos Opcionais:**
  - Email (com validação de formato)
  - Data de Nascimento (formato DD/MM/YYYY)

#### ✨ Recursos:
- Validação de entrada de dados
- Loops até entrada válida
- Exibição de resumo formatado
- Tratamento de Ctrl+C

#### 🏃 Como Usar:
```bash
python3 Code/Concat_dados.py
```

#### 📝 Exemplo de Saída:
```
==================================================
BEM-VINDO AO CONCATENADOR DE DADOS PESSOAIS
==================================================

Digite o nome: João
Digite o sobrenome: Silva
Digite o email (opcional, pressione Enter para pular): joao@email.com
Digite a data de nascimento em DD/MM/YYYY (opcional, pressione Enter para pular): 15/03/1990

==================================================
RESUMO DAS INFORMAÇÕES
==================================================
✓ Nome completo: João Silva
✓ Email: joao@email.com
✓ Data de nascimento: 15/03/1990
==================================================
```

---

### 2️⃣ **repet_txt.py** - Repetidor de Texto

Um programa que recebe um texto e repete sua exibição um número especificado de vezes.

#### 📌 Funcionalidades:
- Coleta um texto do usuário
- Solicita o número de repetições
- Valida número positivo e inteiro
- Exibe com numeração sequencial

#### ✨ Recursos:
- Validação de texto (não pode estar vazio)
- Validação de número inteiro positivo
- Formatação clara com separadores
- Numeração de cada repetição

#### 🏃 Como Usar:
```bash
python3 Code/repet_txt.py
```

#### 📝 Exemplo de Saída:
```
==================================================
REPETIDOR DE TEXTO
==================================================

Digite o texto que deseja repetir: Python é incrível
Quantas vezes você quer repetir? 3

==================================================
RESULTADO DAS REPETIÇÕES
==================================================

1. Python é incrível
2. Python é incrível
3. Python é incrível

==================================================
```

---

### 3️⃣ **oper_mat.py** - Calculadora Matemática

Uma calculadora completa que realiza operações matemáticas básicas e cálculos de porcentagem.

#### 📌 Funcionalidades:

**Operações Básicas:**
1. ➕ **Adição** - Soma dois números
2. ➖ **Subtração** - Subtrai dois números
3. ✖️ **Multiplicação** - Multiplica dois números
4. ➗ **Divisão** - Divide dois números (com proteção contra divisão por zero)

**Operações Avançadas:**
5. 📊 **Porcentagem** - Dois modos:
   - Calcular X% de um valor (ex: 20% de 100)
   - Calcular qual % um valor representa (ex: Quanto % é 20 de 100)

#### ✨ Recursos:
- Menu interativo com emojis
- Validação de entrada numérica
- Proteção contra divisão por zero
- Loop contínuo para múltiplas operações
- Resultados formatados com 2 casas decimais
- Tratamento completo de exceções

#### 🏃 Como Usar:
```bash
python3 Code/oper_mat.py
```

#### 📝 Exemplo de Saída:
```
==================================================
BEM-VINDO À CALCULADORA
==================================================

==================================================
CALCULADORA - ESCOLHA UMA OPERAÇÃO
==================================================
1. ➕ Adição
2. ➖ Subtração
3. ✖️  Multiplicação
4. ➗ Divisão
5. 📊 Porcentagem
6. ❌ Sair
==================================================

Digite a opção (1-6): 1
Digite o primeiro número: 10
Digite o segundo número: 5

10.0 + 5.0 = 15.0
```

---

## 🛠️ Requisitos

- **Python 3.6+** (recomendado 3.8 ou superior)
- Nenhuma biblioteca externa necessária
- Funciona em qualquer sistema operacional (Windows, macOS, Linux)

---

## 📥 Como Começar

### 1. Clone o Repositório:
```bash
git clone https://github.com/Thiago-Emidio-Silva/resolvendo_codigo_py_copilot.git
cd resolvendo_codigo_py_copilot
```

### 2. Execute um Programa:
```bash
# Execute qualquer um dos programas:
python3 Code/Concat_dados.py
python3 Code/repet_txt.py
python3 Code/oper_mat.py
```

---

## 💡 Exemplos de Uso

### Exemplo 1: Concatenando Dados
```bash
$ python3 Code/Concat_dados.py
Digite o nome: Maria
Digite o sobrenome: Santos
Digite o email (opcional): maria@example.com
Digite a data de nascimento: 20/05/1995
# Resultado formatado com todas as informações
```

### Exemplo 2: Repetindo Texto
```bash
$ python3 Code/repet_txt.py
Digite o texto que deseja repetir: Hello World
Quantas vezes você quer repetir? 5
# Texto repetido 5 vezes com numeração
```

### Exemplo 3: Usando a Calculadora
```bash
$ python3 Code/oper_mat.py
# Escolha a operação e realize cálculos
# Suporte a múltiplas operações no mesmo programa
```

---

## 📚 Características Técnicas

Todos os programas compartilham as seguintes características:

### Validação de Entrada:
- Verificação de tipos de dados
- Validação de formatos específicos
- Loops até entrada válida
- Mensagens de erro claras

### Tratamento de Exceções:
- `EOFError` - Entrada finalizada inesperadamente
- `KeyboardInterrupt` - Ctrl+C do usuário
- `ValueError` - Erros de conversão de tipo
- `Exception` - Erros genéricos

### Documentação:
- Docstrings explicativas em todas as funções
- Comentários em linhas importantes
- Descrição de parâmetros e retornos
- Exemplos de uso

### Interface:
- Menus interativos
- Emojis para melhor visualização
- Separadores visuais
- Mensagens de boas-vindas e despedida
- Feedback claro sobre erros

---

## 🎓 Fins Educacionais

Este repositório é ótimo para:
- 📖 Aprender estrutura de código Python
- 🧪 Entender validação de entrada
- ⚙️ Estudar tratamento de exceções
- 📝 Analisar boas práticas de comentários
- 🏗️ Ver organização de funções e módulos

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se livre para:
- Abrir issues com sugestões
- Propor novos programas
- Melhorar a documentação
- Adicionar mais validações

---

## 📝 Licença

Este projeto é fornecido como-é para fins educacionais.

---

## 👨‍💻 Autor

**Thiago Emídio Silva**

---

## 📧 Contato

Para dúvidas ou sugestões sobre os programas, você pode:
- Abrir uma issue no repositório
- Contribuir com melhorias
- Compartilhar feedback

---

## ✅ Checklist de Funcionalidades

- [x] Concatenador de dados pessoais com validação
- [x] Repetidor de texto com entrada de contagem
- [x] Calculadora com 4 operações básicas
- [x] Suporte a cálculos de porcentagem
- [x] Validação completa de entrada
- [x] Tratamento robusto de exceções
- [x] Código comentado em português
- [x] Docstrings em todas as funções
- [x] Interface amigável com emojis
- [x] README detalhado

---

## 🎉 Obrigado por Usar!

Esperamos que esses programas sejam úteis para aprender Python e boas práticas de programação!