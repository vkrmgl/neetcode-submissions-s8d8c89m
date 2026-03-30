class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.minst.append(min(self.minst[-1],val) if self.minst else val)

    def pop(self) -> None:
        self.st=self.st[:-1]
        self.minst=self.minst[:-1]

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
