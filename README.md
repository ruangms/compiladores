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





#TESTES 100% OK


SEQ {
    print("Hello, World!");
}
SEQ {
    a = 5 + 3;
    b = a * 2;
    print(b);
}
SEQ {
    print("Hello, World!");
    a = 5 + 3;
    b = a * 2;
    print(b);
}
SEQ {
    if (x > 10) {
        print("x is greater than 10");
    } else {
        print("x is less than or equal to 10");
    }
}
SEQ {
    while (x < 10) {
        x = x + 1;
    }
    print(x);
}

PAR {
    print("This is parallel process 1");
    print("This is parallel process 2");
}



SEQ {
    g = INPUT();
    a = fibonacci(5);
    print(a);
    print(g);
}
SEQ {
    if (x > 5 and y < 10) {
        print("Condition is true");
    } else {
        print("Condition is false");
    }
}
    

SEQ {
    b = factorial(4);
    print(b);

}


