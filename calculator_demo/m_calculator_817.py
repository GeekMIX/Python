# show __call__ method in calss object and function object in python 

import os


class Calculator():
    def __init__(self, num:int):
        self.state_stack = Stack()
        self.sum_stack = Stack()
        self.text_stack = Stack()
        self.pre_text = "a"
        self.operator_stack = Stack()
        self.num_stack = Stack()
        self.sum = 0
        self.num = num
        '''
        self.state = True  #state indicates whether the current operation is a single number or a combination of operations
        '''           
        self.state_stack.push(True)

        self.cases = {
            "+" : self.add,
            "-" : self.sub,
            "*" : self.mul,
            "/" : self.div,
            "amt" : self.amount,
            "back" : self.back,
            "default" : True,
        }
    def add(self, num:int):
        self.sum += num
        return self
    def sub(self, num:int):
        self.sum -= num
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

        self.sum = self.num_stack.items[0]
        self.all_text = str(self.num_stack.items[0])

        if self.num_stack.size() > 1:
            for i in range(self.operator_stack.size()): 
               self.cases.get(self.operator_stack.items[i])(self.num_stack.items[i+1])  
               self.all_text += self.operator_stack.items[i] + str(self.num_stack.items[i+1])
        return self.sum
    def get_num(self):
        original_text = f"a{self.text_stack.to_string()}"
        new_text = original_text.replace(self.pre_text,"")
        self.pre_text = original_text
        return int(new_text)
        
    def back(self):
        self.sum_stack.pop()
        self.text_stack.pop()
        self.state_stack.pop()


    def get_all_text(self):
        self.all_text = str(self.num_stack.items[0])
        if self.num_stack.size() > 1:
            for i in range(self.operator_stack.size()): 
               self.all_text += self.operator_stack.items[i] + str(self.num_stack.items[i+1])
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

    all_text = "-"
    def __init__(self):
        self.items = []

    def push(self, item:str):
        """向栈中添加一个元素"""
        self.items.append(item)
        Stack.all_text += str(item)

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
    def to_string(self):
        """将栈中的元素转换为字符串"""
        tostr = ""
        for i in range(self.size()):
            tostr += str(self.items[i])
        return tostr
    def clear(self):
        """清空栈"""
        self.items = []

if __name__ == "__main__":
    print(os.path.basename(__file__))




