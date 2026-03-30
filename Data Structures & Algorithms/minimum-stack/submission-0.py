class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr:
            if len(self.arr)==1:
                self.arr=[]
            else:
                self.arr=self.arr[:-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
