# Receber a expressão do usuário
expression = input("Expression: ").strip()

# Definir os operadores possíveis
operators = ["+", "-", "*", "/"]

# Inicializar o resultado como None
result = None

# Iterar sobre os operadores para encontrar o presente na expressão
for operator in operators:
    if operator in expression:
        # Dividir a expressão em dois operandos com base no operador encontrado
        operand1, operand2 = expression.split(operator)

        # Converter os operandos para float
        operand1 = float(operand1.strip())
        operand2 = float(operand2.strip())

        # Realizar a operação de acordo com o operador encontrado
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        break

# Exibir o resultado como ponto flutuante
if result is not None:
    print(float(result))
