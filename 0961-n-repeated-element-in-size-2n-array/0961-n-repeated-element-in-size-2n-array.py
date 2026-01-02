class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = len(nums)
        n = x//2
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
                if cnt[num] == n:
                    return num
