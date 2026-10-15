class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2 and sum(numbers) == target:
            return [1,2]
        i = 0
        j = len(numbers) - 1
        while(numbers[i] + numbers[j] != target and i < j):
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
        return [i+1,j+1]
        