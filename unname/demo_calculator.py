# show __call__ method in calss object and function object in python 

class Calculator():
    def __init__(self, num:int, sum:int = 0, text:str = "", state:bool = True):
        self.num = num 
        self.sum = sum + num
        self.text_stack.peek() = text + f"{num}"   
        '''
        self.state = True  #state indicates whether the current operation is a single number or a combination of operations
        '''    
        self.state = state 
    def add(self, num:int):
        self.text_stack.peek() += f" + {num}"
        self.sum += num
        self.state = False
        return self
    def sub(self, num:int):
        self.text_stack.peek() += f" - {num}"
        self.sum -= num
        self.state = False
        return self
    def div(self, num:int):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        if  self.state:
            self.text_stack.peek() += f" / {num}"
        else:
            self.text_stack.peek() = f"({self.text_stack.peek()}) / {num}"
        self.sum /= num
        self.state = True
        return self
    def mul(self, num:int):
        if   self.state:
            self.text_stack.peek() += f" * {num}"
        else:
            self.text_stack.peek() = f"({self.text_stack.peek()}) * {num}"
        self.sum *= num
        self.state = True
        return self
    def amount(self):
        print(f"{self.text_stack.peek()}  =  {self.sum}")
    

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """向栈中添加一个元素"""
        self.items.append(item)

    def pop(self):
        """从栈顶移除并返回一个元素"""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """查看栈顶元素而不移除它"""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0

    def size(self):
        """返回栈中元素的数量"""
        return len(self.items)


if __name__ == "__main__":
    Calculator(10).mul(5).mul(3).div(7).sub(9).mul(2).amount()




