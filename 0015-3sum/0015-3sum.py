class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        # double two sum
        # for every num in nums solve two sum problem with two pointers
        # num1 + num2 + num3 =0
        #num2 + num3 = 0 - num1
        nums.sort()
        res=[]
        result=None
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            target = -num
            #now two pointers
            left= i+1
            right = n-1
            while left < right:
                if nums[left] + nums[right] < target:
                    left+=1
                elif nums[left] + nums[right] > target:
                    right-=1
                elif nums[left] + nums[right] == target:
                    res.append((num, nums[left], nums[right]))
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                

        return res

    



        