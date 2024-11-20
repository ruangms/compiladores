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

Aqui está uma lista organizada dos testes que você forneceu:

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

Cada um desses testes foi estruturado para verificar funcionalidades diferentes, como a execução de loops, funções recursivas (fatorial, fibonacci), entrada de dados (`INPUT`), condicionais (`if-else`), e execução paralela com o uso do comando `PAR`.
