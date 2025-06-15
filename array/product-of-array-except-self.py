class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        containsZero=False
        zero_indexes=[]
        for num in nums:
            if num !=0:
                product *= num
            else:
                containsZero=True
                zero_indexes.append(nums.index(num))

        print(zero_indexes)
        if not containsZero:
            return [int(product/x) for x in nums]
        elif len(zero_indexes)>1:
            return [0] * len(nums)
        else:
            sol=[]
            for i in range(len(nums)):
                if i in zero_indexes:
                    sol.append(product)
                else:
                    sol.append(0)

            return sol
        

        