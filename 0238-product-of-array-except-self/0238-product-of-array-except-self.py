class Solution(object):
    def productExceptSelf(self, nums):
        '''
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
        '''
        #second way to solve by prefix and sufix
        n=len(nums)
        prefix=[0 for _ in range(n)]
        sufix=[0 for _ in range(n)]
        prefix[0] = nums[0]
        sufix[n-1] = nums[n-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(n-2,-1,-1):
            sufix[i] = sufix[i+1]*nums[i]

        res=[0 for _ in range(n)]
        for i in range(1, n-1):
            res[i] = prefix[i-1] * sufix[i+1]
        res[0] = sufix[1]
        res[n-1] = prefix[n-2]
        return res



