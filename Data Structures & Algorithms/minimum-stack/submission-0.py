class MinStack:
    
    def __init__(self):
        self.values = []
        self.stack = [] 

    def push(self, val: int) -> None:
        self.values.append(val)
        self.stack.append(min(self.values))

    def pop(self) -> None:
        self.values.pop(-1)
        self.stack.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.stack[-1]
        
