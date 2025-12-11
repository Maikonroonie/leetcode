class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        A = [0 for _ in range(2*n)]
        x = 0
        for i in range(n):
            A[x] = nums[i]
            A[x+1] = nums[n+i]
            x+=2
        return A