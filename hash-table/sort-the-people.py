class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = zip(names,heights)
        sorted_d = sorted(d,key=lambda x:x[1],reverse=True)
        return [x[0] for x in sorted_d]