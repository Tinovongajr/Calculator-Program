from tkinter import *
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

def button_press(num):
    global expression
    expression += str(num)
    equation_label.set(expression)

def equals():

    global expression
    try:
        validate_expression(expression)
        ConvertToRPN()
        Calculate()
        Answer= str(stack[0])
        equation_label.set(Answer)
        expression=Answer
    except ZeroDivisionError:
        equation_label.set("Arithmetric error")
    except SyntaxError:
        equation_label.set("Syntax error")
    except Exception as e:
        equation_label.set(e)


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
    equation_label.set("")


window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label= StringVar()

label = Label(window, textvariable=equation_label,font=('consolas'), bg= "white", width= 24, height = 2 )
label.pack()

frame = Frame(window)
frame.pack()

# Buttons
button1= Button(frame, text=1, height=4, width=9, font=35, command=lambda :button_press(1))
button1.grid(row=0, column=0)

button2= Button(frame, text=2, height=4, width=9, font=35, command=lambda :button_press(2))
button2.grid(row=0, column=1)

button3= Button(frame, text=3, height=4, width=9, font=35, command=lambda :button_press(3))
button3.grid(row=0, column=2)

button4= Button(frame, text=4, height=4, width=9, font=35, command=lambda :button_press(4))
button4.grid(row=1, column=0)

button5= Button(frame, text=5, height=4, width=9, font=35, command=lambda :button_press(5))
button5.grid(row=1, column=1)

button6= Button(frame, text=6, height=4, width=9, font=35, command=lambda :button_press(6))
button6.grid(row=1, column=2)

button7= Button(frame, text=7, height=4, width=9, font=35, command=lambda :button_press(7))
button7.grid(row=2, column=0)

button8= Button(frame, text=8, height=4, width=9, font=35, command=lambda :button_press(8))
button8.grid(row=2, column=1)

button9= Button(frame, text=9, height=4, width=9, font=35, command=lambda :button_press(9))
button9.grid(row=2, column=2)

button0= Button(frame, text=0, height=4, width=9, font=35, command=lambda :button_press(0))
button0.grid(row=3, column=0)



plus= Button(frame, text='+', height=4, width=9, font=35, command=lambda :button_press('+'))
plus.grid(row=0, column=3)

minus= Button(frame, text='-', height=4, width=9, font=35, command=lambda :button_press('-'))
minus.grid(row=1, column=3)

multiply= Button(frame, text='*', height=4, width=9, font=35, command=lambda :button_press('*'))
multiply.grid(row=2, column=3)

divide= Button(frame, text='/', height=4, width=9, font=35, command=lambda :button_press('/'))
divide.grid(row=3, column=3)


equal= Button(frame, text='=', height=4, width=9, font=35, command=lambda :equals())
equal.grid(row=3, column=2)

decimal= Button(frame, text='.', height=4, width=9, font=35, command=lambda :button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='Clear', height=4, width=12, font=35, command=lambda:clearx())
clear.pack()



window.mainloop()

