class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        have = set()
        for num in nums:
            have.add(num)
        n = len(nums)
        res = []
        for i in range(1, n+1):
            if i not in have:
                res.append(i)
        return res