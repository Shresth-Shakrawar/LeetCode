class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.count = {}
        self.stack = {}

    def push(self, val: int) -> None:
        newCount = self.count.get(val, 0) + 1
        self.count[val] = newCount

        if newCount > self.maxFreq:
            self.stack[newCount] = []
            self.maxFreq = newCount
        
        self.stack[newCount].append(val)

    def pop(self) -> int:
        val = self.stack[self.maxFreq].pop()
        self.count[val] -= 1
        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1

        return val
        