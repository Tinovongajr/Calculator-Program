
import re
expression=""
RPNexpression=""
stack=[]
RPNlist=[]
operators={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3,
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
            count+=1
            if count >=2:
                raise ValueError("There are two operands following each other")
        else:
            count = 0


    return True

def ConvertToRPN():

    global expression
    global RPNexpression
    global RPNlist
    global stack
    global operators
    stack.clear()
    tempList=[]
    brackets =[')','(']
    bracketOpen=False
    numFlag = 0
    numString = ""
    for index in range(len(expression)):
        i = expression[index]
        if i.isnumeric()or i =='.':
            tempList.append(i)
            numFlag += 1


            if numFlag>1:
                numString=""
                for i in range(numFlag):
                    if len(tempList)>0:
                        num = tempList.pop()
                        if int(num)>9:
                            num = reverseString(num)
                            numString+=num
                        else:
                            numString += str(num)

                tempList.append(reverseString(numString))
                if len(expression) == (index+1) and len(tempList)>0:
                    RPNlist.append(tempList.pop())
                    tempList.clear()
                else:
                    if expression[index +1].isnumeric():
                        pass
                    else:
                        RPNlist.append(tempList.pop())
                        tempList.clear()
            elif numFlag==1 and (index+1) !=len(expression):
                if expression[index+1].isnumeric():
                    pass
                else:
                    RPNlist.append(tempList.pop())
                    tempList.clear()
            elif numFlag==1 and (index+1) ==len(expression):
                RPNlist.append(tempList.pop())
                tempList.clear()


        elif i in operators:

          if len(stack)>=1:

              if operators.get(i) <= operators.get(stack[-1]):
                  while stack and operators.get(i) <= operators.get(stack[-1]):
                    RPNlist.append(stack.pop())

                  stack.append(i)
              else:
                  stack.append(i)
          elif len(stack)==0:
              stack.append(i)



        elif i in brackets:
            numFlag=0
            stack.append(i)
            if i ==')':
                stack.pop()
                lastitem = stack[len(stack) - 1]
                while len(stack) >0  and lastitem!='(':
                    RPNlist.append(stack.pop())
                    lastitem = stack[len(stack) - 1]
                stack.pop()
    else:
       if len(stack)>0:
           for i in range(len(stack)):
              RPNlist.append(stack.pop())

def Calculate():
    global RPNlist
    global stack
    global operators

    #Confirm stack is empty first
    stack.clear()

    for count in range(len(RPNlist)):
        num1=0
        num2=0
        if RPNlist[count].isnumeric():
            stack.append(RPNlist[count])
        elif RPNlist[count] in operators:
            num2= float(stack.pop())
            num1=float(stack.pop())

            if RPNlist[count] == '+':
                stack.append(num1 + num2)
            elif RPNlist[count]=='-':
                stack.append(num1 - num2)
            elif RPNlist[count]=='*':
                stack.append(num1 * num2)
            elif RPNlist[count]=='/':
                stack.append(num1 / num2)
            elif RPNlist[count]=='^':
                stack.append(num1 ** num2)
        #print(stack)

def reverseString(text):
    newText =""
    for i in range(len(text)):
        newText+=text[(len(text)-1)-i]
    return(newText)

def clearx():
    global expression
    global stack
    global RPNlist
    global RPNexpression
    expression = ""
    RPNexpression = ""
    stack = []
    RPNlist = []

def evaluate():
    global expression
    try:
        validate_expression(expression)
        ConvertToRPN()
        Calculate()
        Answer = str(stack[0])
        print(Answer)
        clearx()
    except ZeroDivisionError:
        print("Division by zero error")
    except SyntaxError:
        print("Syntax error")
    except Exception as e:
        print(e)
def main():

    global expression
    print('#'*50)
    print()
    print('******', "Welcome to my Calculator", '******')
    print()
    print("Enter 'w' to stop")
    print()
    print('_'*50)
    print()
    expression = input("Enter an expression : ")
    print()
    while expression != 'w':
        evaluate()
        print()
        expression = input("Enter an expression : ")
main()


