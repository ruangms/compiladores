import re


tokens = [
    (r'[ \t\n]+', None),         # Espaços em branco (ignorados)
    (r'#[^\n]*', None),          # Comentários (ignorados)
    (r'\bprint\b', 'PRINT'),     # Palavra-chave PRINT
    (r'\bSEQ\b', 'SEQ'),         # Palavra-chave SEQ
    (r'\bPAR\b', 'PAR'),         # Palavra-chave PAR
    (r'\bC_CHANNEL\b', 'C_CHANNEL'), # Palavra-chave C_CHANNEL
    (r'\bsend\b', 'SEND'),       # Palavra-chave SEND
    (r'\breceive\b', 'RECEIVE'), # Palavra-chave RECEIVE
    (r'\bfibonacci\b', 'FIBONACCI'), # Palavra-chave FIBONACCI
    (r'\bfactorial\b', 'FACTORIAL'), # Palavra-chave FACTORIAL
    (r'\bcalculate\b', 'CALCULATE'), # Palavra-chave CALCULATE
    (r'[\+\-\*/]', 'OPERATOR'),  # Operadores aritméticos
    (r'\d+\.\d+', 'FLOAT'),      # Números decimais
    (r'\d+', 'INTEGER'),         # Números inteiros
    (r'\(', 'LPAREN'),           # Parêntese esquerdo
    (r'\)', 'RPAREN'),           # Parêntese direito
    (r',', 'COMMA'),             # Vírgula
    (r';', 'SEMI'),              # Ponto e vírgula
    (r'\{', 'LBRACE'),           # Chave aberta
    (r'\}', 'RBRACE'),           # Chave fechada
    (r'\".*?\"', 'STRING'),      # Strings
    (r'\'(.*?)\'', 'STRING'),    # Strings entre aspas simples
    (r'=', 'ASSIGN'),            # Atribuição
    (r'==', 'EQUALS'),           # Igualdade
    (r'!=', 'DIFFERENT'),        # Diferença
    (r'>=', 'GREATEREQUAL'),     # Maior ou igual
    (r'<=', 'LESSEQUAL'),        # Menor ou igual
    (r'>', 'GREATER'),           # Maior que
    (r'<', 'LESS'),              # Menor que
    (r'\band\b', 'AND'),         # Operador lógico AND
    (r'\bor\b', 'OR'),           # Operador lógico OR
    (r'\bnot\b', 'NOT'),         # Operador lógico NOT
    (r'\bif\b', 'IF'),           # Palavra-chave IF
    (r'\belse\b', 'ELSE'),       # Palavra-chave ELSE
    (r'\bwhile\b', 'WHILE'),     # Palavra-chave WHILE
    (r'\bfunction\b', 'FUNCTION'),   # Palavra-chave FUNCTION
    (r'\breturn\b', 'RETURN'),       # Palavra-chave RETURN
    (r'\bINPUT\b', 'INPUT'),         # Palavra-chave INPUT
    (r'\b\w+\b', 'IDENTIFIER'),      # Identificadores (deve vir por último)
]

def lexer(text):
    tokens_list = []
    pos = 0

    while pos < len(text):
        match = None
        for token_regex, token_type in tokens:
            pattern = re.compile(token_regex)
            match = pattern.match(text, pos)
            if match:
                value = match.group(0)
                if token_type:
                    if token_type == 'STRING':
                        value = value[1:-1]  # Remove as aspas
                    tokens_list.append((token_type, value))
                break
        if not match:
            print(f"Token desconhecido: '{text[pos]}'")
        else:
            pos = match.end(0)
    
    return tokens_list

