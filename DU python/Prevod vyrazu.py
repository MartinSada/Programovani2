import sys
sys.setrecursionlimit(10000)

def postfix_to_infix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token in "+":
                infix = f"{operand1}{token}{operand2}"
            else:
                if "+" in operand1 or "-" in operand1 or "*" in operand1 or "/" in operand1:
                    operand1 = f"({operand1})"
                if "+" in operand2 or "-" in operand2 or "*" in operand2 or "/" in operand2:
                    operand2 = f"({operand2})"
                infix = f"{operand1}{token}{operand2}"
            stack.append(infix)

    return stack.pop()

postfix_expression = input()

print(postfix_to_infix(postfix_expression))