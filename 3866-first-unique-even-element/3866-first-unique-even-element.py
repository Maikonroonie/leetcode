class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for num in nums:
            if num % 2 == 0 and d[num] == 1:
                return num
        return -1 
        