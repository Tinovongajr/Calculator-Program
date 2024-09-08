import re

expression = ""
RPNexpression = ""
stack = []
RPNlist = []
operators = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}


def validate_expression(expression):
    if not re.match(r'^[0-9+\-*/^().\s]+$', expression):
        raise ValueError("Invalid characters in expression.")
    if expression[0] in operators:
        raise ValueError("Expression starts with an operator")

    if expression[-1] in operators:
        raise ValueError("Expression ends with an operator.")
    count = 0
    for i in range(len(expression)):
        if expression[i] in operators:
            count += 1
            if count >= 2:
                raise ValueError("There are two operands following each other")
        else:
            count = 0

    return True


def Calculate():
    global RPNlist
    global stack
    global operators

    # Confirm stack is empty first
    stack = []

    for count in range(len(RPNlist)):
        num1 = 0
        num2 = 0
        if RPNlist[count].isnumeric() or '.' in RPNlist[count]:
            stack.append(RPNlist[count])
        elif RPNlist[count] in operators:
            num2 = float(stack.pop())
            num1 = float(stack.pop())

            if RPNlist[count] == '+':
                stack.append(num1 + num2)
            elif RPNlist[count] == '-':
                stack.append(num1 - num2)
            elif RPNlist[count] == '*':
                stack.append(num1 * num2)
            elif RPNlist[count] == '/':
                stack.append(num1 / num2)
            elif RPNlist[count] == '^':
                stack.append(num1 ** num2)


def reverseString(text):
    newText = ""
    for i in range(len(text)):
        newText += text[(len(text) - 1) - i]
    return (newText)


def clearx():
    global expression
    global stack
    global RPNlist
    global RPNexpression
    expression = ""
    RPNexpression = ""
    stack = []
    RPNlist = []


def convertToRPN():
    global expression
    stack = ""
    tempNum = ""

    for index in range(len(expression)):
        i = expression[index]

        if i.isnumeric() or i == '.':
            tempNum += str(i)
            if (len(expression) - index) == 1:
                if tempNum:
                    RPNlist.append(tempNum)
        elif i in ['(', ')']:
            stack += str(i)
            if i == ')':
                stack = stack[:-1]
                if tempNum != "":
                    RPNlist.append(tempNum)
                tempNum = ""
                while stack[-1] != '(' and len(stack) > 1:
                    RPNlist.append(stack[-1])
                    stack = stack[:-1]
                stack = stack[:-1]
        elif i in operators:
            if tempNum:
                RPNlist.append(tempNum)
            if len(stack) < 1 or stack[-1] == '(':
                stack += str(i)
            elif i == stack[-1] and stack[-1] != '(':
                RPNlist.append(i)
            elif stack[-1] != '(':
                if operators.get(i) > operators.get(stack[-1]) and stack[-1] != '(':
                    stack += str(i)
                elif operators.get(i) == operators.get(stack[-1]):
                    RPNlist.append(stack[-1])
                    newStack = stack[:-1]
                    stack = newStack + str(i)
            elif operators.get(i) < operators.get(stack[-1]):
                while operators.get(i) < operators.get(stack[-1]):
                    RPNlist.append(stack[-1])
                    newStack = stack[:-1]
                    stack = newStack + str(i)

            tempNum = ""
    if stack:
        RPNlist.extend([*(reverseString(stack))])


def evaluate():
    global expression
    global stack
    try:

        validate_expression(expression)
        convertToRPN()
        Calculate()

        print("RPN : ", RPNlist)
        print("Answer :  ", str(stack))
        clearx()
    except ZeroDivisionError:
        print("Division by zero error")
    except SyntaxError:
        print("Syntax error")
    except Exception as e:
        print(e)


def main():
    global RPNlist
    global stack
    global expression
    print('#' * 50)
    print()
    print('******', "Welcome to my Calculator", '******')
    print()
    print("Enter 'w' to stop")
    print()
    print('_' * 50)
    print()
    expression = input("Enter an expression : ")
    print()
    expression.strip()
    while expression != 'w':
        evaluate()
        print()
        expression = input("Enter an expression : ")
        stack = []
        RPNlist = []


main()
