class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # counts of residues 0..value-1
        cnt = [0] * value
        for a in nums:
            r = a % value  # Python daje resztę 0..value-1 nawet dla ujemnych
            cnt[r] += 1

        x = 0
        while True:
            r = x % value
            if cnt[r] == 0:
                return x
            cnt[r] -= 1
            x += 1