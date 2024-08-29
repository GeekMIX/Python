# show __call__ method in calss object and function object in python 

class Calculator():
    def __init__(self, num:int):
        self.state_stack = Stack()
        self.sum_stack = Stack()
        self.text_stack = Stack()

        self.num = num 
        self.sum_stack.push(num)
        self.text_stack.push(f"{num}") 
        '''
        self.state = True  #state indicates whether the current operation is a single number or a combination of operations
        '''           
        self.state_stack.push(True)
    def add(self, num:int):
        self.text_stack.push(f" + {num}")
        self.sum_stack.push(self.sum_stack.peek() + num)
        self.state_stack.push(False)
        return self
    def sub(self, num:int):
        self.text_stack.push(f" - {num}")
        self.sum_stack.push(self.sum_stack.peek() - num)
        self.state_stack.push(False)
        return self
    def div(self, num:int):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.sum_stack.push( self.sum_stack.peek() / num)
        self.text_stack.push(f" / {num}")

        self.state_stack.push(True)
        return self
    def mul(self, num:int):
        self.text_stack.push(f" * {num}")
        self.sum_stack.push(self.sum_stack.peek() * num)
        self.state_stack.push(True)
        return self
    def amount(self):               
        print(f"{self.text()}  =  {self.sum_stack.peek()}")
        return self
    def back(self):
        self.sum_stack.pop()
        self.text_stack.pop()
        self.state_stack.pop()

    def text(self):
        text = ""
        for i in range(self.text_stack.size()):   
            if i == 0: 
                text += self.text_stack.items[i]
                continue 
            if self.state_stack.items[i]:
                if self.state_stack.items[i-1]:
                     text += self.text_stack.items[i]
                else:
                    text = f"({text}){self.text_stack.items[i]}"
            else:
                text += self.text_stack.items[i]
        return text

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
    Calculator(10).mul(5).add(2).div(2).back().amount()




