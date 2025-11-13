class Solution:
    def maxSum(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        res = 0
        cnt = 0
        small = -inf
        for num, f in freq.items():
            if num > 0:
                res += num
                cnt += 1
            elif num <= 0:
                small = max(small, num)
        if cnt == 0:
            res += small

        return res
        