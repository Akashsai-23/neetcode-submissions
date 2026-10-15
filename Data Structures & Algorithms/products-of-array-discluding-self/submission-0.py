class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        prod1 = 1
        prod2 = 1
        res = []
        for num in nums:
            prefix_prod.append(prod1)
            prod1 *= num
        for num in nums[::-1]:
            suffix_prod.append(prod2)
            prod2 *= num
        for i in range(len(nums)):
            res.append(prefix_prod[i]*suffix_prod[len(nums)-i-1])
        return res




        
        