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

def ConvertToRPN():

    global expression
    global RPNexpression
    global RPNlist
    global stack
    global operators
    stack.clear()
    tempList=[]
    RPNlist= []
    brackets =[')','(']
    bracketOpen=False
    numFlag = 0
    numString = ""
    isAfterPoint =False
    decimalNums = ""
    for index in range(len(expression)):
        i = expression[index]
        if i.isnumeric() and isAfterPoint==False:
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
            elif numFlag==1 and (index+1) ==len(expression) or expression[index+1] =='.':
                RPNlist.append(tempList.pop())
                tempList.clear()

        elif i.isnumeric() and isAfterPoint==True:
            decimalNums += str(i)

        elif i in operators:

          isAfterPoint = False
          newDecimal = float(RPNlist.pop) + float('0.' + str(decimalNums))
          RPNlist.append(newDecimal)
          if len(stack)>=1:

              if operators.get(i) <= operators.get(stack[-1]):
                  while stack and operators.get(i) <= operators.get(stack[-1]):
                    RPNlist.append(stack.pop())

                  stack.append(i)
              else:
                  stack.append(i)
          elif len(stack)==0:
              stack.append(i)

        elif i =='.':
            isAfterPoint = True

        elif i in brackets:
            numFlag=0
            stack.append(i)
            if i ==')':
                isAfterPoint=False
                newDecimal =  float(RPNlist.pop)+ float('0.'+ str(decimalNums))
                RPNlist.append(newDecimal)
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
    print (RPNlist)
def reverseString(text):
    newText =""
    for i in range(len(text)):
        newText+=text[(len(text)-1)-i]
    return(newText)
def Calculate():
    global RPNlist
    global stack
    global operators

    #Confirm stack is empty first
    stack = []


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


def Evaluate():
    global expression
    try:
        #validate_expression(expression)
        ConvertToRPN()
        Calculate()
        Answer= str(stack[0])
        expression=Answer
        print(expression)
    except ZeroDivisionError:
        print("Division by Zero error")
    except SyntaxError:
        print("Syntax error")
    except Exception as e:
        print(e)
def main():
    global expression
    print ('#'*45)

    print ('*'*5, "Welcome to my calculator App", '*'*5)

    print()
    print("[To cancel input 'w']")
    print("_"*45)
    print()

    expression = input("Enter your Expression : ")
    print()

    while  expression != 'w' :
        Evaluate()
        expression = input("Enter your Expression : ")
        print()

main()












