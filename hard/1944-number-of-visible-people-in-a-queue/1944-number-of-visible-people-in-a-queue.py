            # If smaller in Stack
            while stack and stack[-1] < heights[i]: 
                stack.pop()
                result[i] += 1
            # First Equal or Larger Element
            if stack:
                result[i] += 1
        for i in range(n-1,-1,-1):
        
        result = [0] * n
        stack = []
        n = len(heights)