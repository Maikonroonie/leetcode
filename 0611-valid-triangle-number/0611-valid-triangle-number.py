class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        res = 0
        for k in range(n-1, 1, -1):      # największy bok
            if nums[k] == 0:
                continue
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i         # wszystko między i..j-1 też działa
                    j -= 1
                else:
                    i += 1
        return res
