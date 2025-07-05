class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = [ch for ch in s]
        new_s = [""] * len(s_list)
        for ch,i in zip(s_list,indices):
            new_s[i] = ch
        return "".join(new_s)