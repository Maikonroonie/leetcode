class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        st = set()
        res = 0
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            for j in range(i+1, n):
                num2 = nums[j]
                if num2 == num1:
                    continue
                for k in range(j+1, n):
                    num3 = nums[k]
                    if num1 != num2 and num1 != num3 and num2 != num3:
                        res += 1
        return res