class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        zero_cnt = 0
        zero_place = None
        res=1
        for i in range(n):
            if nums[i] == 0 :
                zero_cnt+=1
                zero_place = i
        if zero_cnt>1:
            return [0 for _ in range(n)]
        if zero_cnt == 1:
            result=[0 for _ in range(n)]
            for i in range(n):
                if i != zero_place:
                    res=res*nums[i]

            result[zero_place] = res
            return result
        else:

            prefix_product=[0 for _ in range(n)]
            prefix_product[0] = nums[0]
            res=[0 for _ in range(n)]
            for i in range(1, n):
                prefix_product[i] = prefix_product[i-1] * nums[i]

            for i in range(n):
                res[i] = prefix_product[n-1]/nums[i]
            
            return res

