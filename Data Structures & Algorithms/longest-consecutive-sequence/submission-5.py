class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for num in nums:
            if num not in s:
                continue
            n = 0
            while(num-1 in s):
                num -= 1
            s.remove(num)
            n += 1
            while(num+1 in s):
                s.remove(num+1)
                num += 1
                n += 1
            if n > m:
                m = n
        return m
            



        