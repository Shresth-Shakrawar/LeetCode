class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        l,r=0,len(people)-1
        while l<=r:
            if people[l] + people[r] <= limit:
                l= l+1
            r=r-1
            boats=boats+1
        return boats