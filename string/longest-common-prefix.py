class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for word in strs:
                if i==len(word):
                    return res
                if word[i] != strs[0][i] :
                    return res
            res= res + strs[0][i]

        #print(res)
        return res            
        