class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] is not 0:
                nums[index] = nums[i]
                if i > index:
                    nums[i] = 0
                index +=1