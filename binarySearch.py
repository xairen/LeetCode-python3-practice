class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            switch = left+(right - left)//2
            if nums[switch] == target:
                return switch
            if target < nums[switch]:
                right = switch - 1
            else:
                left = switch + 1
        return -1