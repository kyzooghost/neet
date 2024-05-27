# All functions should run in O(1) time...this is all straightforward but getMin()
# So you have no space constraints, only time constraints

# Ahh had to use a hint for this zz - also keep track of what is min at each stack change
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(new_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]