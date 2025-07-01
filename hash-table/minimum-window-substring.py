from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = Counter(t)  # Count of chars in t
        window_count = {}
        
        have, need = 0, len(t_count)
        res = [float("inf"), 0, 0]  # window size, left, right
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update result
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                
                # Shrink from left
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""
