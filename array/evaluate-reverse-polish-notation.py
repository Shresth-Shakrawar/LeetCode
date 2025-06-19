class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                b=stack.pop()
                a=stack.pop()
                if s=="+":
                    stack.append(a+b)
                elif s=="-":
                    stack.append(a-b)
                elif s=="*":
                    stack.append(a*b)
                elif s=="/":
                    stack.append(int(a/b))
            #print(f"{s=} {stack=}")
        return stack.pop()


                