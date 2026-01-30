class stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def push(self,Value):
        self.s.append(Value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        else:
            return self.s[-1]

    def pop(self):
         if len(self.s )== 0:
            raise Exception("stack is empty")
         else:
            return self.s.pop(-1)
         
    def display(self):
         if len(self.s )== 0:
            raise Exception("stack is empty")
         else:
             print("elements of stack are:", self.s)

stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.length())
stk.display()
print(stk.peek())
print(stk.pop())