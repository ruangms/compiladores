Projeto de compiladores
-----------------------
*No arquivo teste.py é possivel executar os seguintes testes*

CODIGO ENTRADA:

SEQ {
    g = INPUT("digite aqui o numero a printar ");
    h = INPUT("busque o numero da sequencia de fibonacci ");
    a = fibonacci(h);
    print(g);
    print(a);
}
SEQ {
    print("Hello, World!");
}

# Passo 1: Gerar tokens com o lexer
tokens = lexer(codigo_fonte)
print("Tokens gerados pelo Lexer:")
uio = 0
for token in tokens:
    uio += 1
    print(uio, token)
#Gera uma saida


Tokens gerados pelo Lexer:
1 ('SEQ', 'SEQ')
2 ('LBRACE', '{')
3 ('IDENTIFIER', 'g')
4 ('ASSIGN', '=')
5 ('INPUT', 'INPUT')
6 ('LPAREN', '(')
7 ('STRING', 'digite aqui o numero a printar ')
8 ('RPAREN', ')')
9 ('SEMI', ';')
10 ('IDENTIFIER', 'h')
11 ('ASSIGN', '=')
12 ('INPUT', 'INPUT')
13 ('LPAREN', '(')
14 ('STRING', 'busque o numero da sequencia de fibonacci ')
15 ('RPAREN', ')')
16 ('SEMI', ';')
17 ('IDENTIFIER', 'a')
18 ('ASSIGN', '=')
19 ('FIBONACCI', 'fibonacci')
20 ('LPAREN', '(')
21 ('IDENTIFIER', 'h')
22 ('RPAREN', ')')
23 ('SEMI', ';')
24 ('PRINT', 'print')
25 ('LPAREN', '(')
26 ('IDENTIFIER', 'g')
27 ('RPAREN', ')')
28 ('SEMI', ';')
29 ('PRINT', 'print')
30 ('LPAREN', '(')
31 ('IDENTIFIER', 'a')
32 ('RPAREN', ')')
33 ('SEMI', ';')
34 ('RBRACE', '}')
35 ('SEQ', 'SEQ')
36 ('LBRACE', '{')
37 ('PRINT', 'print')
38 ('LPAREN', '(')
39 ('STRING', 'Hello, World!')
40 ('RPAREN', ')')
41 ('SEMI', ';')
42 ('RBRACE', '}')

# Passo 2: Gerar a AST com o parser
print("\nAST gerada pelo Parser:")
parser = Parser(tokens)
try:
    ast = parser.parse()
    import pprint
    pprint.pprint(ast)
except Exception as e:
    print(f"Erro no parser: {e}")
    
*AST gerada pelo Parser:*
[{'statements': [{'identifier': 'g',
                  'text': 'digite aqui o numero a printar ',
                  'type': 'input'},
                 {'identifier': 'h',
                  'text': 'busque o numero da sequencia de fibonacci ',
                  'type': 'input'},
                 {'identifier': 'a',
                  'type': 'assignment',
                  'value': {'argument': {'type': 'value', 'value': 'h'},
                            'function': 'fibonacci',
                            'type': 'function_call'}},
                 {'items': [{'type': 'identifier', 'value': 'g'}],
                  'type': 'print'},
                 {'items': [{'type': 'identifier', 'value': 'a'}],
                  'type': 'print'}],
  'type': 'SEQ'},
 {'statements': [{'items': [{'type': 'string', 'value': 'Hello, World!'}],
                  'type': 'print'}],
  'type': 'SEQ'}]


# Passo 3: executar a AST com o executor
print("Programa executando")
try:
    ast = parser.parse()
    interpret_ast(ast)
except Exception as e:
    print(f"Erro no parser: {e}")



  *Programa executando*
digite aqui o numero a printar
12
busque o numero da sequencia de fibonacci
12

Resultado:
12
144
Hello, World!





# TESTES 100% OK

### Testes Sequenciais (SEQ)
1. **Teste 1 - SEQ: Fibonacci com impressão**
   ```plaintext
   SEQ {
       print("teste1");
       x = fibonacci(7);
       print(x);
       dfg = 5 + 3;
       print("teste1.1");
   }
   ```

2. **Teste 2 - SEQ: Entrada e Fibonacci**
   ```plaintext
   SEQ {
       g = INPUT("digite aqui o numero a printar ");
       h = INPUT("busque o numero da sequencia de fibonacci ");
       a = fibonacci(h);
       print(g);
       print(a);
   }
   ```

3. **Teste 3 - SEQ: Impressão Simples**
   ```plaintext
   SEQ {
       print("Hello, World!");
   }
   ```

4. **Teste 4 - SEQ: Atribuições e Impressão**
   ```plaintext
   SEQ {
       print("Hello, World!");
       a = 5 + 3;
       b = a * 2;
       print(b);
   }
   ```

5. **Teste 5 - SEQ: Entrada e Fibonacci (repetido)**
   ```plaintext
   SEQ {
       g = INPUT("digite aqui o numero a printar ");
       h = INPUT("busque o numero da sequencia de fibonacci ");
       a = fibonacci(h);
       print(g);
       print(a);
   }
   ```

6. **Teste 6 - SEQ: Impressão Simples (repetido)**
   ```plaintext
   SEQ {
       print("Hello, World!");
   }
   ```

7. **Teste 7 - SEQ: Atribuições e Impressão (repetido)**
   ```plaintext
   SEQ {
       print("Hello, World!");
       a = 5 + 3;
       b = a * 2;
       print(b);
   }
   ```

8. **Teste 8 - SEQ: Condicional**
   ```plaintext
   SEQ {
       print("teste2");
       if (x > 10) {
           print("x is greater than 10");
       } else {
           print("x is less than or equal to 10");
       }
   }
   ```

---

### Testes Paralelos (PAR)
1. **Teste 1 - PAR: Fatorial**
   ```plaintext
   PAR {
       x = 0;
       while (x < 10) {
          x = x + 1;
          v = factorial(x);
          print("@");
          print(v);
       }
       print("teste2");
   }
   ```

2. **Teste 2 - PAR: Fibonacci**
   ```plaintext
   PAR {
       x = 0;
       while (x < 10) {
           x = x + 1;
           v = fibonacci(x);
           print("#");
           print(v);
       }
       print("teste5");
   }
   ```

3. **Teste 3 - PAR: Impressões Paralelas**
   ```plaintext
   PAR {
       print("This is parallel process 1");
       print("This is parallel process 2");
   }
   ```

---
# Estrutura do codigo Parcer

### 1. **Inicialização das Classes**
- **Node**: Representa um nó na árvore de sintaxe, com um tipo (`tipo`), valor (`valor`) e uma lista de filhos (`filhos`).
  - `Node(tipo, valor=None, filhos=None)` — Cria um novo nó com um tipo, um valor e filhos (opcional).

- **Parser**: Classe que implementa a análise sintática de um código baseado em tokens. Recebe uma lista de tokens como entrada.
  - `Parser(tokens)` — Inicializa o parser com os tokens.

### 2. **Funções de Análise (Parsing)**
Estas funções são responsáveis por processar os tokens e construir a árvore de sintaxe:

#### 2.1. **Funções Principais**
- `parse()`: A função principal que começa a análise e gera a árvore sintática (AST). Identifica se os tokens correspondem a um bloco `SEQ` ou `PAR` e chama os métodos correspondentes para processamento.
- `_parse_seq()`: Analisa um bloco de instruções sequenciais (`SEQ`).
- `_parse_par()`: Analisa um bloco de instruções paralelas (`PAR`).

#### 2.2. **Funções de Análise de Comandos**
- `_parse_statements()`: Analisa uma sequência de comandos dentro de um bloco de código. Identifica se é um comando de atribuição, condicional, laço, impressão, retorno, ou comunicação de canal.
  
#### 2.3. **Analisadores de Comandos Específicos**
- `_parse_assignment()`: Analisa um comando de atribuição, seja simples ou com `INPUT`.
- `_parse_expression()`: Analisa uma expressão, incluindo chamadas de funções (como `FIBONACCI` e `FACTORIAL`), valores simples ou operações binárias.
- `_parse_if()`: Analisa uma estrutura condicional `IF`, com a expressão condicional e os ramos verdadeiro e falso.
- `_parse_while()`: Analisa um laço `WHILE`, com a condição de repetição e o corpo do laço.
- `_parse_print()`: Analisa um comando `PRINT`, com expressões que serão impressas.
- `_parse_send_receive()`: Analisa os comandos `SEND` ou `RECEIVE`, processando os operandos dentro dos parênteses.
- `_parse_return()`: Analisa um comando `RETURN`, que retorna um valor de uma expressão.

#### 2.4. **Funções Auxiliares**
- `_match(expected_kind)`: Verifica se o próximo token corresponde ao tipo esperado (`expected_kind`). Se sim, consome o token e avança, caso contrário, gera um erro de sintaxe.
- `_peek()`: Retorna o próximo token sem consumi-lo.
- `id()`: Analisa um identificador (token do tipo `IDENTIFIER`).
- `_parse_binary_operation(left)`: Analisa uma operação binária (como soma, subtração, etc.) entre dois operandos.

### 3. **Funcionalidades Específicas de Token**
O código também lida com uma variedade de tokens, incluindo:
- **Funções**: `FIBONACCI` e `FACTORIAL`.
- **Operadores**: como `+`, `-`, `*`, `>`, `<`, `AND`.
- **Comandos**: `IF`, `WHILE`, `PRINT`, `RETURN`, `SEND`, `RECEIVE`, `C_CHANNEL`.
- **Comandos de Atribuição**: Atribuições simples e a instrução de `INPUT`.
- **Comunicação de Canal**: `C_CHANNEL` (comentado na versão do código).

### 4. **Construção da AST**
A árvore sintática gerada pelo parser terá a estrutura definida pelos métodos de parsing, com um tipo de nó e valores/filhos conforme os comandos e expressões analisadas.

### Exemplo de Saída (AST)
Para um código de entrada simples como:
```plaintext
SEQ {
    x = 5;
    y = x + 3;
    PRINT("Result: ", y);
}
```
A árvore gerada será algo como:
```python
{
    'type': 'SEQ',
    'statements': [
        {'type': 'assignment', 'identifier': 'x', 'value': {'type': 'value', 'value': 5}},
        {'type': 'assignment', 'identifier': 'y', 'value': {'type': 'binary_op', 'operator': '+', 'left': {'type': 'identifier', 'value': 'x'}, 'right': {'type': 'value', 'value': 3}}},
        {'type': 'print', 'items': [{'type': 'string', 'value': 'Result: '}, {'type': 'identifier', 'value': 'y'}]}
    ]
}
```
# GRAMATICA
programa_minipar ::= bloco_stmt
bloco_stmt ::= bloco_SEQ | bloco_PAR
bloco_SEQ ::= SEQ stmts
bloco_PAR ::= PAR stmts
stmts ::= atribuição | if_stmt | while_stmt | send | receive
atribuição ::= id = expr
expr ::= c_channel chan id id_comp1 id_comp2 | expr bin_op expr
bin_op ::= + | - | * | / | > | < | and
if_stmt ::= if ( bool ) stmt | if ( bool ) stmt else stmt
while_stmt ::= while ( bool ) stmt

