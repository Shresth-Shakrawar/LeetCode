class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        #isalnum() checks for number is alphanumerical or not
        while left<right:
            if s[left].isalnum() and s[right].isalnum() and s[left].lower()!=s[right].lower():
                return False
            elif s[left].isalnum() is False:
                left+=1
            elif s[right].isalnum() is False:
                right-=1
            elif s[left].isalnum() and s[right].isalnum() and s[left].lower()==s[right].lower():
                left+=1
                right-=1
            
        return True



        