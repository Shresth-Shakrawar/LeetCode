class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                withoutL=s[l+1:r+1] # l+1 to r
                withoutR=s[l:r]     # l to r-1
                return withoutL == withoutL[::-1] or withoutR == withoutR[::-1]
            
            l,r=l+1,r-1
        return True