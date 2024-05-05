text = input()

def Calculate(text):
    numbers = []
    ops = []

    operators = {"+", "-", "*", "/"}

    for token in reversed(text.split()):
        if token in operators:
            ops.append(token)
        else:
            numbers.append(int(token))
    ops.reverse()

    while ops:
        operand1 = numbers.pop()
        operand2 = numbers.pop()
        token = ops.pop()
        if token == '+':
            numbers.append(operand1 + operand2)
        elif token == '-':
            numbers.append(operand1 - operand2)
        elif token == '*':
            numbers.append(operand1 * operand2)
        elif token == '/':
            if operand2 == 0:
                return "CHYBA"
            else:
                numbers.append(operand1 // operand2)
    return numbers[0]

print(Calculate(text))
