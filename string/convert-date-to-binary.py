class Solution:
    def convertDateToBinary(self, date: str) -> str:
        str_nums = date.split("-")
        nums = [int(x) for x in str_nums]
        binNums = [bin(x)[2:] for x in nums]
        return "-".join(binNums)