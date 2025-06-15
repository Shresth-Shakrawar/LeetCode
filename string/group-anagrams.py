class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict=defaultdict(list) # sortedWords-> List of Words
        for word in strs:
            sorted_word = "".join(sorted(word))
            #print(sorted_word)
            anagramDict[sorted_word].append(word)
        #print(list(anagramDict.values()))
        return list(anagramDict.values())

        
        