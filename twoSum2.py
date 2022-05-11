class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while (left < right):
            newSum = numbers[left] + numbers[right]
            if newSum > target: 
                right -=1
            elif newSum < target: 
                left +=1
            else: 
                return[left+1, right+1]