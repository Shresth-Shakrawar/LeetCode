class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = "".join(str(d) for d in digits)  # convert int to str first
        num = int(str_num)
        num += 1
        str_num2 = str(num)
        num_list = [int(ch) for ch in str_num2]   # convert back to int
        return num_list