class Solution:
    def reverseWords(self, s: str) -> str:
        s_list= s.split(" ")
        sorted_list = [x[::-1] for x in s_list]
        print(f"{sorted_list=}")
        return " ".join(sorted_list)