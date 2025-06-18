class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap={")":"(","}":"{" ,"]":"["}
        stack=[]
        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
            else:
                if stack==[]:
                    return False
                element= stack.pop()
                if bracketMap[bracket] == element:
                    continue
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
