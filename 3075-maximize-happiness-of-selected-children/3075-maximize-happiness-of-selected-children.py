class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse = True)
        res = 0
        #print(happiness[:k])
        for i, num in enumerate(happiness[:k]):
            if num > i:
                res += num - i

        return res

