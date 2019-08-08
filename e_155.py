class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.d.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        x = self.d.pop()
        if self.min_stack and self.min_stack[-1] == x:
            self.min_stack.pop()
        return x

    def top(self) -> int:
        return self.d[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
