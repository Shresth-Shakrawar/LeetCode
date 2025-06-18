class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op=="+":
                element = stack[-1] + stack[-2]
                stack.append(element)
            elif op =="D":
                element = 2 * int(stack[-1])
                stack.append(element)
            elif op=="C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)