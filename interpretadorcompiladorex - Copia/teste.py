from AnalizadorLexico.lexerFuncionando import lexer
from AnalizadorSintatico.parcerFuncionando import Parser
from Executor1 import interpret_ast

# Testando o Lexer e o Parser
codigo_fonte = """



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
    print("teste1");
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
    print("teste2");
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
    g = INPUT("digite um numero");
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