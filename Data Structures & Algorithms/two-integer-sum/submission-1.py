class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i,j = 0, len(nums) - 1
        # while(true):
        #     if (nums[i] + nums[j]) == target:
        #         return [i,j]
        #     if (nums[i] + nums[j]) > target:
        #         i += 1
        #     if (nums[i] + nums[j]) == target:
        #         j += 1
        d = {}
        for idx,num in enumerate(nums):
            d[num] = idx
        for idx,num in enumerate(nums):
            if (target - num) in d and (d[target-num] != idx):
                return [idx,d[target-num]]

        
