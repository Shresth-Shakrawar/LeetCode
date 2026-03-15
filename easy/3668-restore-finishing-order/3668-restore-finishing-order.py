class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for i in range(len(order)):
            if order[i] in friendsSet:
                ans.append(order[i])
        friendsSet=set(friends)
        return ans