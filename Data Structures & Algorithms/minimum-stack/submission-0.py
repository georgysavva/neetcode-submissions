class MinStack:

    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if len(self.min_stack)!=0 else val))

    def pop(self) -> None:
        if len(self.main_stack) == 0:
            return None
        val = self.main_stack[-1]
        self.main_stack=self.main_stack[:-1]
        self.min_stack=self.min_stack[:-1]
        return val

    def top(self) -> int:
        if len(self.main_stack) == 0:
            return None
        return self.main_stack[-1]


    def getMin(self) -> int:
        if len(self.main_stack) ==0:
            return None
        return self.min_stack[-1]
