class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = abs(a) - abs(stack[-1])
                if diff > 0:
                    stack.pop()
                elif diff < 0:
                    a = 0
                else:
                    a=0
                    stack.pop()
            
            if a != 0:
                stack.append(a)
            
        return stack