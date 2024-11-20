import threading
import socket

global_env = {}

def interpretar_programa(ast):
    for bloco in ast:
        if bloco['type'] == 'SEQ':
            executar_seq(bloco['statements'])
        elif bloco['type'] == 'PAR':
            executar_par(bloco['statements'])

def executar_seq(statements):
    for stmt in statements:
        executar_statement(stmt)

def executar_par(statements):
    threads = []
    for stmt in statements:
        t = threading.Thread(target=executar_statement, args=(stmt,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def executar_statement(stmt):
    if stmt['type'] == 'assignment':
        interpretar_atribuicao(stmt)
    elif stmt['type'] == 'print':
        interpretar_print(stmt)
    elif stmt['type'] == 'send':
        interpretar_send(stmt)
    elif stmt['type'] == 'receive':
        interpretar_receive(stmt)

def interpretar_atribuicao(stmt):
    identifier = stmt['identifier']
    value = avaliar_expressao(stmt['value'])
    global_env[identifier] = value

def interpretar_print(stmt):
    for item in stmt['items']:
        if item['type'] == 'identifier':
            print(global_env.get(item['value'], f"Erro: {item['value']} não definido"))
        elif item['type'] == 'string':
            print(item['value'])

def interpretar_send(stmt):
    host, port = "localhost", 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str(stmt['operands']).encode())

def interpretar_receive(stmt):
    host, port = "localhost", 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print("Recebido:", data.decode())

def avaliar_expressao(expr):
    if expr['type'] == 'value':
        return int(expr['value'])
    elif expr['type'] == 'binary_op':
        left = avaliar_expressao(expr['left'])
        right = avaliar_expressao(expr['right'])
        if expr['operator'] == '+':
            return left + right
        elif expr['operator'] == '*':
            return left * right
    elif expr['type'] == 'function_call':
        if expr['function'] == 'fibonacci':
            return calcular_fibonacci(avaliar_expressao(expr['argument']))
        elif expr['function'] == 'factorial':
            return calcular_fatorial(avaliar_expressao(expr['argument']))

def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

def calcular_fatorial(n):
    if n == 0:
        return 1
    return n * calcular_fatorial(n-1)
