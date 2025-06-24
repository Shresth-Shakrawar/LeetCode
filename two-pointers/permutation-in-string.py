class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        def build_count(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            return count

        s1_count = build_count(s1)
        window_count = build_count(s2[:len1])

        if s1_count == window_count:
            return True

        for i in range(len1, len2):
            left = ord(s2[i - len1]) - ord('a')
            right = ord(s2[i]) - ord('a')

            window_count[right] += 1
            window_count[left] -= 1

            if s1_count == window_count:
                return True

        return False
