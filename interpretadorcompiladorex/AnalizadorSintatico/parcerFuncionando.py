class Node:
    def __init__(self, tipo, valor=None, filhos=None):
        self.tipo = tipo
        self.valor = valor
        self.filhos = filhos if filhos else []
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _match(self, expected_kind):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_kind:
            self.pos += 1
            return self.tokens[self.pos - 1]
        raise SyntaxError(f'Expected {expected_kind} at {self.pos}, got {self._peek()}')

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        ast = []
        while self._peek() is not None:
            if self._peek()[0] == 'SEQ':
                ast.append(self._parse_seq())
            elif self._peek()[0] == 'PAR':
                ast.append(self._parse_par())
            else:
                raise SyntaxError(f'Unexpected token: {self._peek()}')
        return ast

    def _parse_seq(self):
        self._match('SEQ')
        self._match('LBRACE')
        stmts = self._parse_statements()
        self._match('RBRACE')
        return {'type': 'SEQ', 'statements': stmts}

    def _parse_par(self):
        self._match('PAR')
        self._match('LBRACE')
        stmts = self._parse_statements()
        self._match('RBRACE')
        return {'type': 'PAR', 'statements': stmts}

    def _parse_statements(self):
        stmts = []
        while self._peek() and self._peek()[0] != 'RBRACE':
            token_type = self._peek()[0]
            if token_type == 'IDENTIFIER':
                stmts.append(self._parse_assignment())
            elif token_type == 'IF':
                stmts.append(self._parse_if())
            elif token_type == 'WHILE':
                stmts.append(self._parse_while())
            elif token_type == 'PRINT':
                stmts.append(self._parse_print())
            elif token_type == 'RETURN':
                stmts.append(self._parse_return())
            elif token_type == 'C_CHANNEL':
                stmts.append(self._parce_c_channel_stmt())
            elif token_type in ('SEND', 'RECEIVE'):
                stmts.append(self._parse_send_receive(token_type))
            else:
                raise SyntaxError(f'Unexpected statement: {self._peek()}')
        return stmts

    def _parse_assignment(self):
        identifier = self._match('IDENTIFIER')[1]
        print(f"Assignment parsing started: identifier={identifier}")

        self._match('ASSIGN')
        if self._peek()[0] == 'INPUT':
            self._match('INPUT')
            self._match('LPAREN')
            p = self._match('STRING')[1]
            self._match('RPAREN')
            self._match('SEMI')
            print(f"Parsed input assignment: identifier={identifier}, text={p}")
            return {'type': 'input', 'identifier': identifier, 'text': p}
        else:
            # Use fallback if expression is not valid
            expression = self._parse_expression()
            if not expression:
                raise SyntaxError("Invalid expression in assignment")
            print(f"Expression parsed: {expression}")
            self._match('SEMI')
            return {'type': 'assignment', 'identifier': identifier, 'value': expression}

    def _parse_expression(self):
        current_token = self._peek()
        print(f"Parsing expression: {current_token}")

        # Funções como FIBONACCI ou FACTORIAL
        if current_token[0] in ('FIBONACCI', 'FACTORIAL'):
            func_name = self._match(current_token[0])[1]
            self._match('LPAREN')
            argument = self._parse_expression()  # Processa o argumento da função
            self._match('RPAREN')  # Fecha o parêntese
            return {'type': 'function_call', 'function': func_name, 'argument': argument}

        # Processa valores simples (inteiros, identificadores ou strings)
        if current_token[0] in ('INTEGER', 'IDENTIFIER', 'STRING'):
            token = self._match(current_token[0])  # Consome o token
            left = {'type': 'value', 'value': token[1]}

            # Verifica se há operadores binários a seguir
            if self._peek() and self._peek()[0] in ('OPERATOR', 'GREATER', 'LESS', 'AND'):
                return self._parse_binary_operation(left)

            return left

        raise SyntaxError(f"Unexpected token in expression: {current_token}")


    def _parse_binary_operation(self, left):
        current_token = self._peek()
        operator = self._match(current_token[0])[1]  # Consome o operador
        right = self._parse_expression()  # Processa a expressão à direita

        return {
            'type': 'binary_op',
            'operator': operator,
            'left': left,
            'right': right
    }



    '''def _parce_c_channel_stmt(self):
        self._match('C_CHANNEL')
        id1_node = self.id()
        id2_node = self.id()
        id3_node = self.id()
        self._match('SEMI')
        return Node('_parce_c_channel_stmt', filhos=[id1_node, id2_node, id3_node])'''
    
    def _parce_c_channel_stmt(self):
        self._match('C_CHANNEL')
        id1_node = self.id()
        id2_node = self.id()
        id3_node = self.id()
        self._match('SEMI')
        return {
        'type': 'c_channel_stmt',
        'operands': [id1_node, id2_node, id3_node]
    }
    
        '''Node(
            tipo='_parce_c_channel_stmt',
            filhos=[
                Node(tipo='identifier', valor=id1_node['value']),
                Node(tipo='identifier', valor=id2_node['value']),
                Node(tipo='identifier', valor=id3_node['value'])
            ]
        )'''


    def id(self):
        token = self._peek()
        if token[0] == 'IDENTIFIER':
            self._match('IDENTIFIER')
            return {'type': 'identifier', 'value': token[1]}
        raise SyntaxError("Expected an identifier")

    def _parse_if(self):
        self._match('IF')
        self._match('LPAREN')
        condition = self._parse_expression()
        self._match('RPAREN')
        self._match('LBRACE')
        true_branch = self._parse_statements()
        self._match('RBRACE')
        false_branch = []
        if self._peek() and self._peek()[0] == 'ELSE':
            self._match('ELSE')
            self._match('LBRACE')
            false_branch = self._parse_statements()
            self._match('RBRACE')
        return {'type': 'if', 'condition': condition, 'true_branch': true_branch, 'false_branch': false_branch}

    def _parse_while(self):
        self._match('WHILE')  # Consome o token 'WHILE'
        self._match('LPAREN')  # Consome '('
        condition = self._parse_expression()  # Processa a condição do laço
        self._match('RPAREN')  # Consome ')'
        self._match('LBRACE')  # Consome '{'

        # Processa o corpo do WHILE
        body = self._parse_statements()  # A função já cuida do laço de instruções

        self._match('RBRACE')  # Consome '}'

        return {
            'type': 'while',
            'condition': condition,
            'body': body
        }
    def _parse_print(self):
        self._match('PRINT')
        self._match('LPAREN')
        print_items = []
        while self._peek() and self._peek()[0] != 'RPAREN':
            if self._peek()[0] == 'STRING':
                value = self._match('STRING')[1]
                print_items.append({'type': 'string', 'value': value})
            elif self._peek()[0] == 'IDENTIFIER':
                identifier = self.id()
                print_items.append(identifier)
            elif self._peek()[0] == 'COMMA':
                self._match('COMMA')
            else:
                raise SyntaxError(f"Unexpected token in PRINT: {self._peek()}")
        self._match('RPAREN')
        self._match('SEMI')
        return {'type': 'print', 'items': print_items}


    def _parse_send_receive(self, kind):
        self._match(kind)
        self._match('LPAREN')
        operands = []
        while self._peek() and self._peek()[0] not in ('RPAREN', 'SEMI'):
            operands.append(self._parse_expression())
            if self._peek() and self._peek()[0] == 'COMMA':
                self._match('COMMA')
        self._match('RPAREN')
        self._match('SEMI')
        return {'type': kind.lower(), 'operands': operands}

    def _parse_return(self):
        self._match('RETURN')
        value = self._parse_expression()
        self._match('SEMI')
        return {'type': 'return', 'value': value}
