class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        lst = [[] for i in range(len(nums))]
        res = []
        for num in nums:
            d[num] = d.get(num,0) + 1
        for key, value in d.items():
            lst[value-1].append(key)
        for i in lst[::-1]:
            res.extend(i)
        return res[:k] 

        