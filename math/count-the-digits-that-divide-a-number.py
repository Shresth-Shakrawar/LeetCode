class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        ans = 0
        for ch in num_str:
            if num % int(ch) == 0:
                ans += 1
        return ans