class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack : list[(int,int)] = [] # (num,index)

        for i,temp in enumerate(temperatures):
            #print(f"Before Popping {stack=}")
            while stack and stack[-1][0] < temp : 
                stackT , stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex # Append (index of higher temp - index of stack element)

            stack.append((temp , i))
            #print(f"After Popping {stack=} {res=}")
        return res