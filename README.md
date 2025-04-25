# Compilador JARO

<div align="center">
    <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
    <img src="https://img.shields.io/badge/plataforma-unix%20%7C%20linux%20%7C%20macos-lightgrey" alt="Plataforma">
    <img src="https://img.shields.io/badge/arquitetura-arm-green" alt="ARM">
    <img src="https://img.shields.io/badge/status-estável-brightgreen" alt="Status: Estável">
</div>

## 📋 Índice

- [Compilador JARO](#compilador-jaro)
  - [📋 Índice](#-índice)
  - [🚀 Sobre o Projeto](#-sobre-o-projeto)
  - [🏗 Estrutura do Compilador](#-estrutura-do-compilador)
    - [Arquivos do Projeto](#arquivos-do-projeto)
  - [📝 A Linguagem](#-a-linguagem)
    - [Estrutura Básica](#estrutura-básica)
    - [Tipos de Dados](#tipos-de-dados)
    - [Comandos](#comandos)
    - [Operadores](#operadores)
  - [💻 Instalação e Requisitos](#-instalação-e-requisitos)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
  - [🖱 Como Usar](#-como-usar)
    - [Opções Disponíveis](#opções-disponíveis)
    - [Exemplos de Uso](#exemplos-de-uso)
  - [📊 Exemplos de Programas](#-exemplos-de-programas)
    - [Exemplo 1: Programa Simples](#exemplo-1-programa-simples)
    - [Exemplo 2: Cálculo de Fibonacci](#exemplo-2-cálculo-de-fibonacci)
  - [🔄 Fases de Compilação](#-fases-de-compilação)
    - [1. Análise Léxica](#1-análise-léxica)
    - [2. Análise Sintática](#2-análise-sintática)
    - [3. Análise Semântica](#3-análise-semântica)
    - [4. Geração de Código Intermediário](#4-geração-de-código-intermediário)
    - [5. Geração de Código Final](#5-geração-de-código-final)
  - [📁 Arquivos de Log e Saída](#-arquivos-de-log-e-saída)
  - [👥 Contribuidores](#-contribuidores)

## 🚀 Sobre o Projeto

Este projeto implementa um compilador completo para uma linguagem personalizada chamada JARO. O compilador realiza todas as fases clássicas de um processo de compilação, desde a análise léxica até a geração de código Assembly ARM.

O Compilador JARO foi desenvolvido como trabalho para a disciplina de Compiladores, demonstrando conceitos fundamentais de teoria da compilação e implementação prática de compiladores.

## 🏗 Estrutura do Compilador

O compilador possui uma arquitetura modular, dividida nas seguintes etapas:

1. **Análise Léxica** - Converte o código fonte em tokens
2. **Análise Sintática** - Verifica se a sequência de tokens segue a gramática da linguagem
3. **Análise Semântica** - Verifica a coerência semântica do programa
4. **Geração de Código Intermediário** - Cria uma representação intermediária do código
5. **Geração de Código Final** - Traduz a representação intermediária para código Assembly ARM

### Arquivos do Projeto

- `Compilador.py` - Arquivo principal que integra todas as etapas
- `AnaliseLexica.py` - Implementa o analisador léxico
- `AnaliseSintatica.py` - Implementa o analisador sintático
- `AnaliseSemantica.py` - Implementa o analisador semântico
- `Codigo_Intermediario.py` - Gera o código intermediário
- `Codigo_Final.py` - Gera o código Assembly final
- `infixa_posfixa.py` - Converte expressões infixas para posfixas
- `*.txt` e `*.s` - Arquivos de exemplo e saída

## 📝 A Linguagem

A linguagem JARO é uma linguagem simples com sintaxe inspirada em Python. Suas principais características são:

### Estrutura Básica

```
inicio;
        // código aqui
fim;
```

### Tipos de Dados

- `int` - Números inteiros

### Comandos

- Leitura: `leia(variavel);`
- Escrita: `escreva(variavel);`
- Condicional: `se (condição) entao ... senao ... fimse;`
- Repetição: `enquanto (condição) faca (expressão);`

### Operadores

- Aritméticos: `+`, `-`, `*`, `/`
- Relacionais: `=`, `>`

## 💻 Instalação e Requisitos

### Pré-requisitos

- Python 3.9 ou superior
- Sistema operacional Unix/Linux/macOS
- Processador ARM ou emulador ARM

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/joaooliveira10/Compiladores
   cd Compiladores
   ```

2. Nenhuma dependência externa é necessária para executar o compilador

## 🖱 Como Usar

O compilador pode ser executado via linha de comando com diferentes opções:

```bash
python Compilador.py [opções] arquivo_entrada [arquivo_saida]
```

### Opções Disponíveis

- `-lt, --lt`: Mostra a lista de tokens do analisador léxico
- `-ls, --ls`: Mostra o log do analisador sintático
- `-lse, --lse`: Mostra o log do analisador semântico
- `-ts, --ts`: Exibe a tabela de símbolos
- `-lgcI, --lgcI`: Exibe o log do código intermediário
- `-lgcF, --lgcF`: Exibe o log do código final
- `-lgc, --lgc`: Exibe os logs de código intermediário e final
- `-tudo, --tudo`: Mostra todas as listagens do compilador

### Exemplos de Uso

```bash
# Compilar arquivo e mostrar todas as etapas
python Compilador.py -tudo exemplo.txt exemplo.s

# Ver apenas a análise léxica
python Compilador.py -lt exemplo.txt

# Ver a tabela de símbolos
python Compilador.py -ts exemplo.txt
```

## 📊 Exemplos de Programas

### Exemplo 1: Programa Simples

```
inicio;
        int cont;
        leia (cont);
        escreva (cont);
        int a;
        a : (69);
        int b;
        b : (26);
        se (a > b) entao
                escreva (a);
                senao
                escreva (b);
        fimse;
fim;
```

### Exemplo 2: Cálculo de Fibonacci

```
inicio;
        int i : 0;
        int n : 0;
        int auxiliar : 0;
        int a : 0;
        int b : 1;

        leia(n);
        escreva(b);
        n : n - 1;

        enquanto
                auxiliar : (a + b);
                a : b;
                b : auxiliar;
                escreva(auxiliar);
                i : i + 1;
        faca (n > i);
fim;
```

## 🔄 Fases de Compilação

### 1. Análise Léxica

O analisador léxico (`AnaliseLexica.py`) lê o código fonte caracter por caracter e o converte em uma sequência de tokens. Ele implementa um autômato finito determinístico para reconhecer os padrões léxicos da linguagem.

### 2. Análise Sintática

O analisador sintático (`AnaliseSintatica.py`) verifica se a sequência de tokens está em conformidade com a gramática da linguagem. Utiliza uma abordagem de análise descendente recursiva com tabela de parsing.

### 3. Análise Semântica

O analisador semântico (`AnaliseSemantica.py`) verifica a coerência semântica do programa, como verificação de tipos, declaração de variáveis antes do uso e prevenção de divisões por zero.

### 4. Geração de Código Intermediário

A fase de geração de código intermediário (`Codigo_Intermediario.py`) traduz o programa para uma representação intermediária mais próxima do código alvo, facilitando otimizações.

### 5. Geração de Código Final

A geração de código final (`Codigo_Final.py`) traduz a representação intermediária para código Assembly ARM, que pode ser montado e executado em plataformas compatíveis.

## 📁 Arquivos de Log e Saída

O compilador gera diversos arquivos de log durante o processo de compilação:

- `log_operacoes.txt` - Log de operações do analisador semântico
- `log_intermediario.txt` - Log da geração de código intermediário
- `log_final.txt` - Log da geração de código final
- `arquivo_intermediario.txt` - Código intermediário gerado
- `*.s` - Arquivo de saída com código Assembly ARM

Para executar o código Assembly gerado:

1. Compile o arquivo `.s` com gcc:
   ```bash
   gcc -o programa programa.s
   ```
2. Execute o programa resultante:
   ```bash
   ./programa
   ```

## 👥 Contribuidores

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de Compiladores.
