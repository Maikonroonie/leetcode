class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(1, n+1):
            d[i] = 0
        for num in nums:
            d[num] += 1
        for n, t in d.items():
            if t == 2:
                a = n
            elif t == 0:
                b = n
        return (a, b)
        

