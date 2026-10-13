class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx,num in enumerate(nums):
            d[num] = idx
        for idx,num in enumerate(nums):
            if (target - num) in d and (d[target-num] != idx):
                return [idx,d[target-num]]

        
