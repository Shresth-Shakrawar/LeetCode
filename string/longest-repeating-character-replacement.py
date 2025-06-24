class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charSet = set(s)
        maxLength = 0
        
        for c in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l) + 1 - count > k : # length of window - count of char > maximum replacements allowed
                    if s[l] == c:
                        count -= 1
                    l+=1
                maxLength =  max(maxLength,(r-l+1))

        return maxLength 

