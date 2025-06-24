class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = {} # Count of Characters In Windows
        max_length = 0

        maxfreq = 0
        l = 0
        
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r],0) + 1
            maxfreq = max(maxfreq,charCount[s[r]])
            
            while (r-l) + 1 - maxfreq > k : # length - maxfreq gives Number of other characters which are not most frequent
                charCount[s[l]] -=1
                l+=1
            
            max_length = max((r-l) + 1,max_length)

            
        return max_length

