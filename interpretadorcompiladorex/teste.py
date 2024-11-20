from AnalizadorLexico.lexerFuncionando import lexer
from AnalizadorSintatico.parcerFuncionando import Parser
from Executor1 import interpret_ast

# Testando o Lexer e o Parser
codigo_fonte = """

SEQ {
  #  print("teste1");
 #   x = fibonacci(7);
#    print(x);

    dfg = 5 + 3;
    print("teste1.1");

}
PAR {
    o = 0;
    while (o < 10) {
       o = o + 1;
       v = factorial(o);
       print("@");
       print(v);
    }
    print("tste1212212");
}
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
SEQ {
    print("Hello, World!");
    a = 5 + 3;
    b = a * 2;
    print(b);
}

PAR {
    print("This is parallel process 1");
    print("This is parallel process 2");
}



SEQ {
    print("teste2");
    if (x > 10) {
        print("x is greater than 10");
    } else {
        print("x is less than or equal to 10");
    }
}


SEQ {
    if (x > 5 and y < 10) {
        print("Condition is true");
    } else {
        print("Condition is false");
    }
}


"""

# Passo 1: Gerar tokens com o lexer
tokens = lexer(codigo_fonte)
print("Tokens gerados pelo Lexer:")
uio = 0
for token in tokens:
    uio += 1
    print(uio, token)

# Passo 2: Gerar a AST com o parser
print("\nAST gerada pelo Parser:")
parser = Parser(tokens)
try:
    ast = parser.parse()
    
    import pprint
    pprint.pprint(ast)
    print("Programa executando")
    interpret_ast(ast)
except Exception as e:
    print(f"Erro no parser: {e}")


'''

'''