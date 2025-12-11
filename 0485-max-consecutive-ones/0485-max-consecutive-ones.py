class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_len = 0
        max_len = 0
        for num in nums:
            if num == 1:
                cur_len +=1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 0
        max_len = max(cur_len, max_len)
        return max_len
