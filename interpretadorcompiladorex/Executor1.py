import threading

# Função para calcular o fatorial
def factorial(n):
    n = int(n)
    def funcao(n):
        if n == 0 or n == 1:
            return 1
        return n * funcao(n - 1)
    return funcao(n)

# Função para calcular Fibonacci
def fibonacci(n):
    n = int(n)
    def funcao(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return funcao(n - 1) + funcao(n - 2)
    return funcao(n)

# Interpretador principal
class Interpreter:
    def __init__(self):
        self.variables = {}
        self.channels = {}

    def evaluate(self, expr):
        if expr["type"] == "value":
            # Verificando se o valor é uma string e convertendo para inteiro se necessário
            try:
                return int(expr["value"])  # Converte se for numérico
            except ValueError:
                if expr["value"] in self.variables:
                    variable_value = self.variables[expr["value"]]
                    if isinstance(variable_value, str) and variable_value.isdigit():
                        return int(variable_value)
                    return variable_value  # Variável existente
                return expr["value"]  # Retorna string ou valor literal

        elif expr["type"] == "identifier":
            return self.variables.get(expr["value"], None)
        elif expr["type"] == "binary_op":
            left = self.evaluate(expr["left"])
            right = self.evaluate(expr["right"])
            operator = expr["operator"]

        # Certifique-se de que left e right sejam numéricos quando necessário
            if isinstance(left, str) and left.isdigit():
                   left = int(left)
            if isinstance(right, str) and right.isdigit():
                    right = int(right)
    

            if operator == "+":
                return left + right
            elif operator == "*":
                return left * right
            elif operator == ">":
                return left > right
            elif operator == "<":
                return left < right
            elif operator == "and":
                return left and right
        return None



    def execute_statement(self, stmt):
        if stmt["type"] == "input":
            self.variables[stmt["identifier"]] = input(stmt["text"])
        elif stmt["type"] == "assignment":
            if stmt["value"]["type"] == "value":
                value = self.evaluate(stmt["value"])
                #print(f"Assigning {stmt['identifier']} = {value}")  # Log da atribuição
                self.variables[stmt["identifier"]] = value
            elif stmt["value"]["type"] == "function_call":
                func = stmt["value"]["function"]
                arg = self.evaluate(stmt["value"]["argument"])
                if func == "fibonacci":
                    self.variables[stmt["identifier"]] = fibonacci(arg)
                elif func == "factorial":
                    self.variables[stmt["identifier"]] = factorial(arg)
            elif isinstance(stmt["value"], dict) and stmt["value"].get("type") == "binary_op":
                # A expressão binária é avaliada e o resultado é armazenado
                result = self.evaluate(stmt["value"])
                #print(f"Assigning {stmt['identifier']} = {result}")  # Imprime a atribuição
                self.variables[stmt["identifier"]] = result
            else:
                raise ValueError("Assignment value is not a valid expression")

        elif stmt["type"] == "print":
            values = [self.evaluate(item) if item["type"] == "identifier" else item["value"] for item in stmt["items"]]
            print(" ".join(map(str, values)))
        elif stmt["type"] == "if":
            condition = self.evaluate(stmt["condition"])
            branch = stmt["true_branch"] if condition else stmt["false_branch"]
            for s in branch:
                self.execute_statement(s)
        elif stmt["type"] == "while":
            while self.evaluate(stmt["condition"]):
                for s in stmt["body"]:
                    self.execute_statement(s)
        elif stmt["type"] == "send":
            channel, value = stmt["operands"]
            if channel["value"] not in self.channels:
                self.channels[channel["value"]] = []
            self.channels[channel["value"]].append(self.evaluate(value))
        elif stmt["type"] == "receive":
            channel, target = stmt["operands"]
            if channel["value"] in self.channels and self.channels[channel["value"]]:
                self.variables[target["value"]] = self.channels[channel["value"]].pop(0)

    def execute(self, node):
        if node["type"] == "SEQ":
            for stmt in node["statements"]:
                self.execute_statement(stmt)
        elif node["type"] == "PAR":
            threads = []
            for stmt in node["statements"]:
                thread = threading.Thread(target=lambda: self.execute_statement(stmt))
                threads.append(thread)
                thread.start()


# Interpretação de uma AST completa
def interpret_ast(ast):
    interpreter = Interpreter()
    for node in ast:
        interpreter.execute(node)

