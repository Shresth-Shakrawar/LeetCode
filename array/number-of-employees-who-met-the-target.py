class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for h in hours:
            if h >= target:
                ans += 1
        return ans