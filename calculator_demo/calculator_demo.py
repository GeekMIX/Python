import os
from m_calculator_816 import Calculator


first_number = input("input the first integer\n->: ")
calculator = Calculator(int(first_number))



cases = {
    "add" : calculator.add,
    "sub" : calculator.sub,
    "mul" : calculator.mul,
    "div" : calculator.div,
    "amt" : calculator.amount,
    "back" : calculator.back,
    "default" : True,

}

invalid_operator = {
    "add" : False,
    "sub" : False,
    "mul" : False,
    "div" : False,
    "amt" : False,
    "back" : False,
    "default" : True,
}

def tips():
    print("add +\nsub -\nmul *\ndiv /\namt =\nback back operation")

      

while True:
    operator = input("input your operator\n->: ")
    ## amount calculator ##
    if operator == "exit":
        break

    if operator == "amt":
        calculator.amount()
        continue
    ## back operation ##
    if operator == "back":
        if calculator.state_stack.size() > 1:
            calculator.back()
            print(calculator.text())
            continue
        else:
            first_number = input("input the first integer\n->: ")
            calculator.num = int(first_number)
            continue
    ## invalid operator ##

    operator_p = operator.split()
    if invalid_operator.get(operator_p[0],"default"):
        print("invalid operator")
        tips()
        continue
    else:
        if len(operator_p) > 1:      
            for i in range(0, len(operator_p), 2):
                next_number = operator_p[i+1]
                calculator = cases.get(operator_p[i])(int(next_number))
        else:
            next_number = input("input the next integer\n->: ")
            calculator = cases.get(operator_p[0])(int(next_number))
        print(calculator.text())      

## pause ##
os.system("pause")