class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # n ^3 is the best we can do here
        nums.sort()
        n=len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]
            for j in range(n-1, i+2, -1):
                if j < n - 1 and nums[j] == nums[j+1]:
                    continue
                n2 = nums[j]
                new_target = target - n1 - n2
                l = i+1
                r = j-1
                while l < r:
                    current_sum = nums[l] + nums[r]
                    
                    if current_sum == new_target:
                        res.append([n1, nums[l], nums[r], n2])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                            
                    elif current_sum < new_target:
                        l += 1
                    else:
                        r -= 1
                        
        return res
        