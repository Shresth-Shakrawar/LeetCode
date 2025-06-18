class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        res=0
        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                #print(f"Removed {s[l]=} from {charSet=}")
                l+=1
                

            charSet.add(s[r])
            #print(f"Added {s[r]=} to {charSet=}")
            res = max(res,r-l+1)
            #print(f"Result for {r=} is {res=}")

        return res
