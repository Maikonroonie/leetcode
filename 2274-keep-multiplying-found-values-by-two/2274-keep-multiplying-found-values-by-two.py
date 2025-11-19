class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        set_of_nums = set()
        for num in nums:
            if num not in set_of_nums:
                set_of_nums.add(num)
        while True:
            if original not in set_of_nums:
                return original
            else:
                original *= 2
                
        
        