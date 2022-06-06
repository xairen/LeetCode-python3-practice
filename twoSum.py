class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            tn = target - num
            if tn in result.keys():
                return [result[tn], i]
            else:
                result[num] = i
