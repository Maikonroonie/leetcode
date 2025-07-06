class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        left = 0
        right = n-1
        while left<right:
            while numbers[left] + numbers[right] > target:
                right-=1
            while numbers[left] + numbers[right] < target:
                left+=1 
            if numbers[left] + numbers[right] == target:
                return left+1, right+1