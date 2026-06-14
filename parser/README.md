# Trabalho de Teoria da Computação: Linguagem para Planilhas de Treinamento de Corrida

## Grupo
- Guilherme Souza da Roza Lobato - Cartão UFRGS: 584649
- Thiago Noll da Fontoura - Cartão UFRGS: 601238
- Vinícius Witt Herzog - Cartão UFRGS: 589261

Olá! Este é o nosso trabalho para a disciplina de Teoria da Computação. Nele, desenvolvemos uma Linguagem Específica de Domínio (DSL) utilizando Python e a biblioteca `ply` (Python Lex-Yacc) para modelar planilhas de treinamento de corrida.

## A Nossa Ideia (Descrição do Domínio)
Nós queríamos criar uma linguagem que nos permitisse organizar rotinas de corrida em blocos de calendário bem definidos: Meses, Semanas e Dias. Além disso, queríamos a capacidade de construir rotinas com laços de repetição (`REPETIR`) que pudessem ser aninhados de forma arbitrária em qualquer nível (Mês, Semana, Dia ou até no próprio Treino).

Ao contrário de uma calculadora convencional que apenas avalia uma expressão matemática escalar, a nossa linguagem constrói e processa uma árvore estruturada de múltiplos atributos simultâneos. Durante a execução (feita de dentro para fora pelo parser ascendente LALR), o interpretador:
1. Valida o balanceamento estrutural das chaves (garantindo que cada bloco foi aberto e fechado corretamente).
2. Sintetiza, a cada escopo resolvido, não apenas a quilometragem (km) total daquele bloco, mas também o tempo total de descanso (min).
3. Soma esses valores em listas/sequências e os multiplica quando encontra um bloco de repetição.

## Como a biblioteca PLY funciona e os arquivos gerados
Neste trabalho, utilizamos a biblioteca `ply` que divide a construção do compilador/interpretador em duas partes:
- **`lex.py` (Lexer)**: Analisa o arquivo de texto e o quebra em pedaços chamados *tokens* (como `MES`, `REPETIR`, `NUMERO`, chaves, etc.). No nosso código, isso está no arquivo `regex.py`.
- **`yacc.py` (Parser)**: Pega esses tokens e verifica se eles formam uma estrutura válida baseada nas regras de derivação (Backus-Naur Form). Isso está no arquivo `regras.py`.

### O que são `parser.out` e `parsetab.py`?
A biblioteca `ply` gera esses dois arquivos automaticamente na primeira vez que executamos o parser:
- **`parsetab.py`**: É a tabela de parsing (estados e transições) pré-computada para o método LALR(1). Ela fica salva para que o programa não precise recalcular toda a máquina de estados a cada execução, melhorando o desempenho.
- **`parser.out`**: É um arquivo de log (texto humano) gerado para ajudar no debug do parser. Ele mostra todos os estados, as regras da gramática, shift/reduce conflicts (se houver) e como a máquina de estados avalia as transições.

## Como rodar o projeto no Linux (ou Windows)

### Requisitos
- **Python 3.x** instalado.
- **Biblioteca `ply`** instalada. Para instalar, abra o terminal e execute:
  ```bash
  pip install ply
  ```

### Execução Detalhada
O programa funciona lendo um arquivo de texto contendo a planilha de treinos (input) e gerando um arquivo de texto com o resultado calculado ou a mensagem de erro (output).

Para executar, você precisa passar dois argumentos na linha de comando: o caminho do arquivo de entrada e o caminho do arquivo de saída.

1. Abra o terminal e navegue até a pasta `parser` do projeto:
   ```bash
   cd parser
   ```
2. Execute o programa usando o comando `python` (ou `python3` no Linux, ou `py` no Windows) chamando o `main.py` e informando os caminhos dos arquivos:
   ```bash
   python main.py ../data/input_0.txt ../data/output_0.txt
   ```
O programa avisará no próprio terminal se o arquivo foi aceito (sintaxe correta) ou rejeitado (sintaxe incorreta). O resultado detalhado estará no arquivo `output_0.txt`.

### Como criar seu próprio arquivo de input para testar

1. Vá até a pasta `data/` (ou qualquer pasta de sua preferência) e crie um arquivo de texto com a extensão `.txt`, por exemplo: `meu_treino.txt`.
2. Escreva o seu código respeitando a nossa gramática. Por exemplo:
   ```text
   MES "Agosto" {
       SEMANA 1 {
           REPETIR 3 {
               DIA "Treino" {
                   CORRER 5 KM FORTE
                   DESCANSAR 10 MIN
               }
           }
       }
   }
   ```
3. Salve o arquivo.
4. Volte ao terminal, na pasta `parser/`, e execute o programa apontando para o seu arquivo novo e definindo o nome do arquivo de saída desejado:
   ```bash
   python main.py ../data/meu_treino.txt ../data/resultado_meu_treino.txt
   ```
5. Verifique o terminal para ver se foi `[ACEITO]` ou `[REJEITADO]`.
6. Abra o arquivo `resultado_meu_treino.txt` (que será gerado na pasta `data/`) para ver o relatório final com a soma da quilometragem e minutos!