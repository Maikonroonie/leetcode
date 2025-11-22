class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        def is_g(a):
            if a % 3 == 0:
                return True
            return False
        
        n = len(nums)
        p = 0
        while True:
            if p == n-1 and is_g(nums[p]):
                return res
            elif is_g(nums[p]):
                p+=1
            else:
                res += 1
                if nums[p] % 3 == 1:
                    nums[p] -= 1
                else:
                    nums[p] += 1
        return res




        