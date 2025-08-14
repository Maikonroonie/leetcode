class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        n=len(nums)
        cnt=[inf for _ in range(n)]
        cnt[0] = 0
        for i, jump in enumerate(nums):
            if i > far:           # nie doskoczyliśmy do i
                return False
            far = max(far, i + jump)
            for x in range(1, jump+1):
                if i+x < n:
                    cnt[i+x] = min(cnt[i+x], cnt[i] + 1)
                
        return cnt[n-1]

