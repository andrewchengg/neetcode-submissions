class MinStack:
    
    def __init__(self):
        self.values = []
        self.stack = [] 

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.stack or val < self.stack[-1]: #if value is less than the min
            self.stack.append(val)
        else: 
            self.stack.append(self.stack[-1])

    def pop(self) -> None:
        self.values.pop(-1)
        self.stack.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.stack[-1]
        
